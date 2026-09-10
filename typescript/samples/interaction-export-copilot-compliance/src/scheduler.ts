// ─── Scheduled polling using node-cron ───

import cron from 'node-cron';
import { exportInteractions } from './graph-export';
import { createLogger } from './logger';

const log = createLogger('Scheduler');

let task: cron.ScheduledTask | null = null;

export function startScheduler(): void {
    const schedule = process.env.EXPORT_CRON ?? '0 */1 * * *'; // default: every hour
    const userId = process.env.USER_ID;

    if (!userId) {
        log.warn('USER_ID not set — scheduler disabled');
        return;
    }

    task = cron.schedule(schedule, async () => {
        log.info('Scheduled export triggered');
        try {
            const count = await exportInteractions({ userId });
            log.info(`Scheduled export finished — ${count} interactions`);
        } catch (err) {
            log.error(`Scheduled export failed: ${(err as Error).message}`);
        }
    });

    log.info(`Scheduler started with cron: ${schedule}`);
}

export function stopScheduler(): void {
    if (task) {
        task.stop();
        task = null;
        log.info('Scheduler stopped');
    }
}
