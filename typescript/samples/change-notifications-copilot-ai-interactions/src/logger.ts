// ============================================================
// logger.ts
// Lightweight structured logger with levels, timestamps, and
// component tags. Configured via the LOG_LEVEL env var.
//
// Usage:
//   import { createLogger } from "./logger";
//   const log = createLogger("Server");
//   log.info("Listening on port 3000");
//   log.error("Something broke", { statusCode: 500 });
// ============================================================

/** Supported log levels (ordered by severity). */
export enum LogLevel {
    DEBUG = 0,
    INFO = 1,
    WARN = 2,
    ERROR = 3,
}

/** Map level names → enum values for env-var parsing. */
const LEVEL_NAMES: Record<string, LogLevel> = {
    debug: LogLevel.DEBUG,
    info: LogLevel.INFO,
    warn: LogLevel.WARN,
    error: LogLevel.ERROR,
};

/** ANSI colour codes for pretty terminal output. */
const COLORS: Record<LogLevel, string> = {
    [LogLevel.DEBUG]: "\x1b[36m", // cyan
    [LogLevel.INFO]: "\x1b[32m",  // green
    [LogLevel.WARN]: "\x1b[33m",  // yellow
    [LogLevel.ERROR]: "\x1b[31m", // red
};
const RESET = "\x1b[0m";
const BOLD = "\x1b[1m";

/** Human-readable labels. */
const LABELS: Record<LogLevel, string> = {
    [LogLevel.DEBUG]: "DEBUG",
    [LogLevel.INFO]: " INFO",
    [LogLevel.WARN]: " WARN",
    [LogLevel.ERROR]: "ERROR",
};

/** Read the active log level from `LOG_LEVEL` env var (default: INFO). */
function resolveLevel(): LogLevel {
    const raw = (process.env.LOG_LEVEL || "info").toLowerCase().trim();
    return LEVEL_NAMES[raw] ?? LogLevel.INFO;
}

/** A logger instance scoped to a named component. */
export interface Logger {
    debug(message: string, meta?: Record<string, unknown>): void;
    info(message: string, meta?: Record<string, unknown>): void;
    warn(message: string, meta?: Record<string, unknown>): void;
    error(message: string, meta?: Record<string, unknown>): void;
    /** Print a horizontal separator line at INFO level. */
    separator(): void;
    /** Print a blank line at INFO level. */
    blank(): void;
    /** Print key-value detail lines (indented) at INFO level. */
    details(pairs: Record<string, unknown>): void;
}

/**
 * Create a logger for a specific component.
 *
 * ```ts
 * const log = createLogger("Webhook");
 * log.info("Notification received", { subscriptionId: "abc" });
 * // => 2026-03-02T10:15:30.123Z  INFO [Webhook] Notification received  {"subscriptionId":"abc"}
 * ```
 */
export function createLogger(component: string): Logger {
    const minLevel = resolveLevel();

    function emit(
        level: LogLevel,
        message: string,
        meta?: Record<string, unknown>
    ): void {
        if (level < minLevel) return;

        const timestamp = new Date().toISOString();
        const colour = COLORS[level];
        const label = LABELS[level];
        const tag = `${BOLD}[${component}]${RESET}`;
        const metaStr = meta && Object.keys(meta).length > 0
            ? `  ${JSON.stringify(meta)}`
            : "";

        const line = `${timestamp} ${colour}${label}${RESET} ${tag} ${message}${metaStr}`;

        if (level >= LogLevel.ERROR) {
            console.error(line);
        } else if (level >= LogLevel.WARN) {
            console.warn(line);
        } else {
            console.log(line);
        }
    }

    return {
        debug: (msg, meta?) => emit(LogLevel.DEBUG, msg, meta),
        info: (msg, meta?) => emit(LogLevel.INFO, msg, meta),
        warn: (msg, meta?) => emit(LogLevel.WARN, msg, meta),
        error: (msg, meta?) => emit(LogLevel.ERROR, msg, meta),

        separator(): void {
            if (LogLevel.INFO < minLevel) return;
            console.log("=".repeat(60));
        },

        blank(): void {
            if (LogLevel.INFO < minLevel) return;
            console.log();
        },

        details(pairs: Record<string, unknown>): void {
            if (LogLevel.INFO < minLevel) return;
            const maxKey = Math.max(...Object.keys(pairs).map((k) => k.length));
            for (const [key, value] of Object.entries(pairs)) {
                console.log(`   ${key.padEnd(maxKey)} : ${value}`);
            }
        },
    };
}
