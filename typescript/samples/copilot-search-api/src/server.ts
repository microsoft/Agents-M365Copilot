import express, { Request, Response } from 'express';
import dotenv from 'dotenv';
import {
  performSearch,
  searchWithPathFilter,
  buildPathFilter,
} from './search';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/health', (_req: Request, res: Response) => {
  res.json({ status: 'OK' });
});

app.post(
  '/api/search',
  async (req: Request, res: Response) => {
    try {
      const { query, pageSize, skipToken, filterExpression } =
        req.body;

      const options: any = {};

      if (pageSize) options.pageSize = pageSize;
      if (skipToken) options.skipToken = skipToken;
      if (filterExpression)
        options.filterExpression = filterExpression;

      const result = await performSearch(query, options);

      res.json(result);
    } catch (error: any) {
      res.status(500).json({
        success: false,
        error: error?.message,
      });
    }
  }
);

app.post(
  '/api/search/path',
  async (req: Request, res: Response) => {
    try {
      const { query, oneDrivePath } = req.body;

      const result = await searchWithPathFilter(
        query,
        oneDrivePath
      );

      res.json(result);
    } catch (error: any) {
      res.status(500).json({
        success: false,
        error: error?.message,
      });
    }
  }
);

app.listen(PORT, () => {
  console.log(
    `Copilot Search API running at http://localhost:${PORT}`
  );
});