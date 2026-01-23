/**
 * API client for backend communication
 */

const API_BASE = import.meta.env.VITE_API_URL || 'https://api.pradanayahya.com';

// ============ Contact ============

export interface ContactData {
    name: string;
    email: string;
    message: string;
}

export async function submitContact(data: ContactData) {
    const response = await fetch(`${API_BASE}/api/contact`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (!response.ok) {
        throw new Error('Failed to submit contact form');
    }

    return response.json();
}

// ============ Chat ============

export interface ChatMessage {
    role: 'user' | 'assistant';
    content: string;
}

export interface ChatResponse {
    session_id: string;
    answer: string;
    sources: Array<{
        category: string;
        title: string;
        score: number;
    }>;
}

export async function createChatSession(): Promise<{ session_id: string }> {
    const response = await fetch(`${API_BASE}/api/chat/session`, {
        method: 'POST',
    });

    if (!response.ok) {
        throw new Error('Failed to create chat session');
    }

    return response.json();
}

export async function sendChatMessage(
    message: string,
    sessionId?: string
): Promise<ChatResponse> {
    const response = await fetch(`${API_BASE}/api/chat`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message,
            session_id: sessionId,
        }),
    });

    if (!response.ok) {
        throw new Error('Failed to send message');
    }

    return response.json();
}

export async function getChatHistory(sessionId: string): Promise<{
    session_id: string;
    messages: Array<{
        role: string;
        content: string;
        created_at: string;
    }>;
}> {
    const response = await fetch(`${API_BASE}/api/chat/session/${sessionId}/messages`);

    if (!response.ok) {
        throw new Error('Failed to get chat history');
    }

    return response.json();
}

// ============ Admin Auth ============

export async function adminLogin(username: string, password: string) {
    const response = await fetch(`${API_BASE}/api/admin/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
        throw new Error('Invalid credentials');
    }

    return response.json();
}

export async function adminLogout() {
    const response = await fetch(`${API_BASE}/api/admin/logout`, {
        method: 'POST',
        credentials: 'include',
    });

    return response.json();
}

export async function checkAdminAuth() {
    const response = await fetch(`${API_BASE}/api/admin/me`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Not authenticated');
    }

    return response.json();
}

// ============ Admin Data ============

export async function getContacts() {
    const response = await fetch(`${API_BASE}/api/admin/contacts`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get contacts');
    }

    return response.json();
}

export async function getContact(id: string) {
    const response = await fetch(`${API_BASE}/api/admin/contacts/${id}`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get contact');
    }

    return response.json();
}

export async function markContactRead(id: string) {
    const response = await fetch(`${API_BASE}/api/admin/contacts/${id}/read`, {
        method: 'PATCH',
        credentials: 'include',
    });

    return response.json();
}

export async function deleteContact(id: string) {
    const response = await fetch(`${API_BASE}/api/admin/contacts/${id}`, {
        method: 'DELETE',
        credentials: 'include',
    });

    return response.json();
}

export async function getChats() {
    const response = await fetch(`${API_BASE}/api/admin/chats`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get chats');
    }

    return response.json();
}

export async function getChat(id: string) {
    const response = await fetch(`${API_BASE}/api/admin/chats/${id}`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get chat');
    }

    return response.json();
}

export async function deleteChat(id: string) {
    const response = await fetch(`${API_BASE}/api/admin/chats/${id}`, {
        method: 'DELETE',
        credentials: 'include',
    });

    return response.json();
}

export async function getStats() {
    const response = await fetch(`${API_BASE}/api/admin/stats`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get stats');
    }

    return response.json();
}

// ============ Ingest ============

export async function getIngestFiles() {
    const response = await fetch(`${API_BASE}/api/admin/ingest/files`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get files');
    }

    return response.json();
}

export async function getIngestFile(filename: string) {
    const response = await fetch(`${API_BASE}/api/admin/ingest/files/${filename}`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get file');
    }

    return response.json();
}

export async function createIngestFile(filename: string, content: any[]) {
    const response = await fetch(`${API_BASE}/api/admin/ingest/files`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ filename, content }),
    });

    if (!response.ok) {
        throw new Error('Failed to create file');
    }

    return response.json();
}

export async function updateIngestFile(filename: string, content: any[]) {
    const response = await fetch(`${API_BASE}/api/admin/ingest/files/${filename}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ content }),
    });

    if (!response.ok) {
        throw new Error('Failed to update file');
    }

    return response.json();
}

export async function deleteIngestFile(filename: string) {
    const response = await fetch(`${API_BASE}/api/admin/ingest/files/${filename}`, {
        method: 'DELETE',
        credentials: 'include',
    });

    return response.json();
}

export async function syncToQdrant() {
    const response = await fetch(`${API_BASE}/api/admin/ingest/sync`, {
        method: 'POST',
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to sync');
    }

    return response.json();
}

export async function getIngestStatus() {
    const response = await fetch(`${API_BASE}/api/admin/ingest/status`, {
        credentials: 'include',
    });

    if (!response.ok) {
        throw new Error('Failed to get status');
    }

    return response.json();
}
