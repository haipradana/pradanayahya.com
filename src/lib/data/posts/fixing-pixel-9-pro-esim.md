My Pixel 9 Pro could use a physical SIM normally, but adding an eSIM ended with the same unhelpful message: **“SIM not activated.”** Scanning a QR code or entering the activation details manually led back to the same screen.

The useful clue was buried in Android's testing menu: the eUICC reported **available memory of `-1`**. That led me to a community repair method that updates the firmware of the secure element used by the eSIM.

These are my notes, rewritten as a step-by-step walkthrough. The method requires root access and careful firmware selection. The data-preserving path below assumes the bootloader is **already unlocked**.

## Before you start

**Back up your important data first.** Preserving photos and apps does not mean preserving everything stored on the secure element. The updater can erase eSIM profiles, digital car keys, and FeliCa data, and it can change the EID. Arrange access to your carrier's eSIM replacement process before proceeding.

If your bootloader is locked, stop here if keeping your current data is essential. Unlocking or relocking it wipes user data; [Android's bootloader documentation](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) explains this behavior.

Choosing an incompatible secure-element firmware can leave eSIM functionality unusable. Do not proceed through a compatibility warning or guess a firmware from its name.

### Setup recorded in my notes

| Component | Recorded setup |
| --- | --- |
| Device | Google Pixel 9 Pro, `caiman` |
| Android build | Android 17, `CP3A.260905.009` |
| Root tool | Official Magisk v31.0 |
| Secure-element configuration | ST54, `P24_ST54L` |
| Previous firmware | `GGL_P24_ST54L_GSMALIVE_DVT_CG7_v2` |
| Firmware used for the repair | `GGL_P24_ST54L_GSMALIVE_534-1.1_DVT_CG7_v2` |
| Starting bootloader state | Already unlocked |

These values describe this setup. Check your own model, installed build, chip information, and updater warnings before using any image or firmware label below.

## Step 1: Check the eUICC status

Open the Phone app and enter:

```text
*#*#4636#*#*
```

Choose **Phone information** and find **eUICC info**. The value that prompted this repair was:

```text
{ Available memory in bytes:-1 }
```

A `-1` result is a reason to investigate the eUICC, rather than repeatedly requesting activation codes. It does not establish the cause on every device. If the menu reports a positive memory value, investigate the carrier, activation code, and device eligibility before attempting this firmware procedure.

I kept the repair focused on the eSIM component. This walkthrough does not require a factory reset, flashing the modem, or installing an entire factory image.

## Step 2: Prepare the phone and computer

You will need a computer with Google's [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools), a reliable USB data cable, and a stable Wi-Fi connection on the phone. Charge the phone before starting.

Enable **USB debugging** in Developer options. Connect the phone, approve the debugging prompt, and check the connection from your computer:

```bash
adb devices
```

The phone should appear with the status `device`. If it says `unauthorized`, unlock the screen and accept the authorization prompt.

Confirm the device and installed build:

```bash
adb shell getprop ro.product.device
adb shell getprop ro.build.id
```

For the device in these notes, the codename is `caiman`. A Pixel 9 Pro XL is `komodo`; its image is not interchangeable with the Pixel 9 Pro image.

Enter the bootloader to inspect its state:

```bash
adb reboot bootloader
```

Read **Device state** on the phone. Continue with this data-preserving route only if it already says **unlocked**. An enabled OEM unlocking toggle alone does not establish this. If unlocking is unavailable, check the device's restrictions before going further.

Return to Android:

```bash
fastboot reboot
```

## Step 3: Download the matching factory image

Get the factory image for your exact device and **currently installed build** from [Google's official factory-image page](https://developers.google.com/android/images). In this workflow, the archive supplies one stock image to patch; do not run its full flashing script.

Compare the archive's **complete SHA-256 checksum** with Google's published value. A short filename suffix is not a substitute for that comparison.

On Linux:

```bash
sha256sum your-downloaded-factory-image.zip
```

On macOS:

```bash
shasum -a 256 your-downloaded-factory-image.zip
```

Replace the example filename with your download. Extract the factory archive, then the inner `image-caiman-…zip` archive, and locate **`init_boot.img`**.

Keep an untouched copy on your computer. For the Pixel 9 Pro setup here, `init_boot.img` is the image to patch.

## Step 4: Patch your own image with Magisk

Install Magisk from the [official project releases](https://github.com/topjohnwu/Magisk/releases). My notes use v31.0; its [release notes](https://github.com/topjohnwu/Magisk/releases/tag/v31.0) include Android 17 Zygisk support. Check the project's current instructions when working with a different Android build.

Copy your matching stock image to the phone:

```bash
adb push init_boot.img /sdcard/Download/init_boot.img
```

In Magisk:

1. Tap **Install** in the Magisk card.
2. Choose **Select and Patch a File**.
3. Select the `init_boot.img` you copied.
4. Wait for the patching process to finish.
5. Note the exact output filename shown in the installation log.

Copy that output back to the computer, replacing this example with the actual filename:

```bash
adb pull /sdcard/Download/magisk_patched-xxxxx.img ./magisk_patched.img
```

Patch the image **on the phone that will use it**. Do not download another person's patched image. See [Magisk's installation guide](https://topjohnwu.github.io/Magisk/install.html) for the official patching procedure.

## Step 5: Flash the patched init_boot image

From the directory containing your patched image, run:

```bash
adb reboot bootloader
fastboot devices
```

Confirm that fastboot sees the intended phone and that its bootloader remains unlocked. Then flash only the prepared image:

```bash
fastboot flash init_boot magisk_patched.img
fastboot reboot
```

After Android starts, open Magisk and confirm that it shows an installed version. Complete any setup it requests before continuing.

**Do not run `flash-all.sh`, `flash-all.bat`, `fastboot -w`, or a bootloader lock/unlock command as part of these steps.** They are outside this procedure and can wipe your data.

Root remains installed after a reboot at this point. The later cleanup step removes it.

## Step 6: Prepare a root shell for the updater

Open an Android shell from the computer:

```bash
adb shell
su
```

Approve the superuser request on the phone. Run the following commands individually in that **root shell**:

```sh
resetprop ro.build.type eng
resetprop ro.build.tags eng
resetprop ro.debuggable 1
setenforce 0
```

Then restart the Android framework:

```sh
stop && sleep 2 && start
```

The screen will restart while Android's framework comes back. If the shell disconnects, reconnect with `adb shell` and `su`. Keep Wi-Fi connected and **do not perform a full reboot yet**.

These commands temporarily change runtime properties and put SELinux into permissive mode. That reduces protection during the procedure. Keep this interval short and avoid installing software or granting unrelated root access. A normal reboot restores these runtime changes on the stock setup described here; it does not uninstall Magisk.

## Step 7: Open the secure-element firmware updater

From the root shell, launch the updater activity:

```sh
am start -n com.google.euiccpixel/com.google.euiccpixel.ui.OtaUpdateMenu
```

The phone should open the **NFC/eSE/eSIM firmware updater**. The dialer code `*#*#3987#*#*` is another entry point recorded in my notes; availability depends on the installed software.

Read **SE information** before selecting anything. For this setup, the relevant configuration was `P24_ST54L` on an ST54 secure element.

In **Upgrade firmware**, the entry used in these notes was:

```text
GGL_P24_ST54L_GSMALIVE_534-1.1_DVT_CG7_v2
```

Use the production **`GSMALIVE`** family appropriate to the device. Do not substitute a **`GSMATEST`** entry or a label for another hardware generation. Leave **Owner ID** and **Part number** at their defaults, which were blank in this setup.

Tap **SE FIRMWARE UPGRADE** to open the confirmation dialog. Read that dialog before authorizing the actual update.

## Step 8: Check the confirmation, then update

Cancel if the updater warns that you selected the same image again, that the image is incompatible or non-compliant, or that it may break the device. If the correct entry is missing, stop and check the original guide rather than cycling through firmware choices.

The dialog should identify the expected current and new firmware and explain what will be erased. Matching names alone are not proof of compatibility: the chip configuration, intended production firmware, and compatibility checks must all agree.

Make sure you understand the eSIM-profile deletion and any EID change. Once you have verified those details, tap **CONTINUE**.

During the update:

- Stay on the updater screen.
- Keep Wi-Fi and power stable.
- Leave the USB cable connected.
- Do not reboot or interrupt the process.

My notes allow roughly two to three minutes, but follow the updater's status rather than a timer. Wait for **Update complete** and check the reported firmware label before continuing.

## Step 9: Reboot and check the result

Exit the root shell, then the Android shell:

```sh
exit
exit
```

Back in your computer's terminal, reboot the phone:

```bash
adb reboot
```

Return to `*#*#4636#*#*` → **Phone information** → **eUICC info**. The expected change is a **positive available-memory value** instead of `-1`.

You can also check SELinux from the computer:

```bash
adb shell getenforce
```

On the stock setup described here, it should report `Enforcing` after reboot. Investigate an unexpected result before returning the phone to normal use.

## Step 10: Activate a replacement eSIM

If the update reset your profiles or changed the EID, use your carrier's replacement or reissue process. Ask whether a new QR code or activation code is required; reuse rules differ between carriers.

Connect to stable Wi-Fi and try activation again. A positive memory value is one useful check, while successful installation and a working mobile connection are the practical confirmation.

For an imported phone in Indonesia, check the registration and eligibility of the IMEI used for eSIM with your carrier. Physical-SIM service alone does not settle that question. Follow the carrier's own migration instructions when converting an existing physical SIM.

## Step 11: Remove root when you are finished

If you installed Magisk only for this repair, use **Magisk → Uninstall → Complete Uninstall**. The app's uninstall path is described in the [official installation documentation](https://topjohnwu.github.io/Magisk/install.html#uninstallation). Keep your original matching image available in case restoration is needed.

After uninstalling and rebooting, check the eUICC status and your eSIM connection again.

Treat bootloader relocking as a separate recovery decision. It wipes data and requires a correctly restored, compatible system. Do not relock a modified installation as a casual cleanup step. Leaving it unlocked also has security consequences and may affect integrity checks used by payment, banking, or other apps.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| ADB reports `unauthorized` | Unlock the phone and approve the computer's debugging request. |
| `su` is denied | Check that Magisk is installed and that the shell has permission in its Superuser settings. |
| The phone will not boot after patching | If the patched image is the cause, restoring your original, matching `init_boot.img` may recover boot. See the commands below. |
| The updater will not open | Check that the root-shell commands completed and that you did not fully reboot between framework preparation and launching the updater. |
| No clearly compatible firmware appears | Stop. Recheck the exact hardware configuration and the community guide. |
| The update fails or eUICC still reports `-1` | Record the error and check the device/build-specific discussion. Avoid repeatedly flashing firmware without understanding the failure. |
| eUICC memory is positive, but activation fails | Check the carrier's activation-code status, replacement process, network connection, and device eligibility. |

To restore the stock image **only when it matches the currently installed build**, enter the bootloader using the phone's buttons, then run from the computer:

```bash
fastboot devices
fastboot flash init_boot init_boot.img
fastboot reboot
```

This is a recovery option for a bad patched image, not a guarantee for every boot failure. Do not expand the repair to unrelated partitions or wipe commands without a separate recovery plan.

## Credits and further reading

The secure-element repair method comes from **JSPiRiT's community guide**, linked below. This article records a specific Pixel 9 Pro setup; it does not establish an official Google repair procedure or a diagnosis for every failed eSIM activation.

- [JSPiRiT: Fix Pixel eSIM / eUICC on XDA](https://xdaforums.com/t/guide-fix-pixel-esim-euicc.4797083/), the original community guide referenced by my notes.
- [Official Pixel factory images](https://developers.google.com/android/images), for device/build-matched downloads and Google's flashing cautions.
- [Official Android Platform Tools](https://developer.android.com/tools/releases/platform-tools), for ADB and fastboot.
- [Magisk installation documentation](https://topjohnwu.github.io/Magisk/install.html) and [official releases](https://github.com/topjohnwu/Magisk/releases), for patching and removal.
- [Android bootloader locking and unlocking](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking), for device-state and data-wipe behavior.

If the firmware labels, warnings, or device behavior differ from this setup, pause and investigate those differences before continuing.
