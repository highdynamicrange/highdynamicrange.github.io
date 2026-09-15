import {defineCollection} from 'astro:content';
import {glob} from 'astro/loaders';
import {z} from 'astro/zod';
export const collections={archive:defineCollection({loader:glob({pattern:'**/*.md',base:'./src/content/archive'}),schema:z.object({title:z.string(),summary:z.string(),date:z.coerce.date().optional(),source:z.string()})})};
