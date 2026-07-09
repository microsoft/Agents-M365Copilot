import React from 'react';
import ReactDOM from 'react-dom/client';
import { MsalProvider } from '@azure/msal-react';
import { getMsalInstance } from './auth/msalConfig';
import { AuthProvider } from './auth/AuthProvider';
import App from './App';
import './index.css';

(async () => {
    const msalInstance = await getMsalInstance();

    // Handle the auth response (redirect or popup return).
    try {
        const response = await msalInstance.handleRedirectPromise();
        if (response) {
            msalInstance.setActiveAccount(response.account);
        }
    } catch (err) {
        console.error('MSAL redirect error:', err);
    }

    // If there are already accounts, set the first as active.
    const accounts = msalInstance.getAllAccounts();
    if (accounts.length > 0 && !msalInstance.getActiveAccount()) {
        msalInstance.setActiveAccount(accounts[0]);
    }

    ReactDOM.createRoot(document.getElementById('root')!).render(
        <React.StrictMode>
            <MsalProvider instance={msalInstance}>
                <AuthProvider>
                    <App />
                </AuthProvider>
            </MsalProvider>
        </React.StrictMode>,
    );
})();
