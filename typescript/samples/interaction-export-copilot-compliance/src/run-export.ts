// ─── One-shot manual export runner ───
// Usage: npm run export

import 'dotenv/config';
import { initDatabase } from './database';
import { exportInteractions } from './graph-export';
import { createLogger } from './logger';

const log = createLogger('RunExport');

async function main() {
    const userId = process.env.USER_ID;
    if (!userId) {
        log.error('USER_ID is required in .env');
        process.exit(1);
    }

    initDatabase();

    log.info(`Starting export for user ${userId} …`);
    const count = await exportInteractions({ userId });
    log.info(`✅ Export complete — ${count} interactions archived`);
}

main().catch((err) => {
    log.error(`Export failed: ${err.message}`);
    process.exit(1);
});
