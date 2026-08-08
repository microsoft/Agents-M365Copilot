// ─── Structured logger with levels, timestamps, and component tags ───

type LogLevel = 'debug' | 'info' | 'warn' | 'error';

const LEVEL_PRIORITY: Record<LogLevel, number> = { debug: 0, info: 1, warn: 2, error: 3 };
const LEVEL_ICONS: Record<LogLevel, string> = { debug: '🔍', info: '📘', warn: '⚠️', error: '❌' };

const currentLevel: LogLevel = (process.env.LOG_LEVEL as LogLevel) ?? 'info';

function shouldLog(level: LogLevel): boolean {
    return LEVEL_PRIORITY[level] >= LEVEL_PRIORITY[currentLevel];
}

function format(level: LogLevel, component: string, message: string): string {
    const ts = new Date().toISOString();
    return `${ts} ${LEVEL_ICONS[level]} [${level.toUpperCase().padEnd(5)}] [${component}] ${message}`;
}

export function createLogger(component: string) {
    return {
        debug: (msg: string) => shouldLog('debug') && console.debug(format('debug', component, msg)),
        info: (msg: string) => shouldLog('info') && console.log(format('info', component, msg)),
        warn: (msg: string) => shouldLog('warn') && console.warn(format('warn', component, msg)),
        error: (msg: string) => shouldLog('error') && console.error(format('error', component, msg)),
    };
}
