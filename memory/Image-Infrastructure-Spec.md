---
title: "Featured Image Infrastructure Specification"
description: "Technical spec for implementing featured images across all 7 sites"
category: "Technical"
author: "Seb"
publishedDate: "2026-04-05"
---

# Featured Image Infrastructure
## Phase 2 Implementation

---

## 1. Frontmatter Schema

### Standard Featured Image Fields

```yaml
featuredImage:
  src: "/images/hero-recipe-carbonara.jpg"  # Required: path to image
  alt: "Creamy carbonara pasta in white bowl"  # Required: descriptive alt text
  credit: "Unsplash"  # Optional: attribution
  photographer: "Name"  # Optional: photographer name
  caption: "Authentic Roman carbonara"  # Optional: caption for below image
  focalPoint: "center"  # Optional: for cropping (top, center, bottom)
```

### Extended Fields (Optional)

```yaml
featuredImage:
  src: "/images/recipe.jpg"
  alt: "Description"
  dimensions:
    width: 1920
    height: 1080
    aspectRatio: "16:9"
  optimization:
    lazyLoad: true
    placeholder: "blur"  # blur, color, or none
    sizes: [640, 1024, 1920]  # responsive srcset
```

---

## 2. Component Architecture

### FeaturedImage.tsx Component

```typescript
// components/FeaturedImage.tsx
import Image from 'next/image';

interface FeaturedImageProps {
  src: string;
  alt: string;
  caption?: string;
  credit?: string;
  priority?: boolean;  // for above-the-fold images
  className?: string;
}

export function FeaturedImage({
  src,
  alt,
  caption,
  credit,
  priority = false,
  className = ""
}: FeaturedImageProps) {
  return (
    <figure className={`featured-image ${className}`}>
      <Image
        src={src}
        alt={alt}
        width={1200}
        height={675}
        priority={priority}
        className="w-full h-auto rounded-lg"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 800px"
      />
      {(caption || credit) && (
        <figcaption className="text-sm text-gray-500 mt-2">
          {caption && <span>{caption}</span>}
          {credit && <span className="ml-2">Photo: {credit}</span>}
        </figcaption>
      )}
    </figure>
  );
}
```

### ArticleHeader.tsx Component

```typescript
// components/ArticleHeader.tsx
import { FeaturedImage } from './FeaturedImage';

interface ArticleHeaderProps {
  title: string;
  description?: string;
  featuredImage?: {
    src: string;
    alt: string;
    caption?: string;
    credit?: string;
  };
  category?: string;
  readingTime?: string;
}

export function ArticleHeader({
  title,
  description,
  featuredImage,
  category,
  readingTime
}: ArticleHeaderProps) {
  return (
    <header className="article-header mb-8">
      {category && (
        <span className="category-badge">{category}</span>
      )}
      <h1 className="text-3xl md:text-4xl font-bold mt-2 mb-4">{title}</h1>
      {description && (
        <p className="text-xl text-gray-600 mb-4">{description}</p>
      )}
      {readingTime && (
        <span className="text-sm text-gray-500">{readingTime} min read</span>
      )}
      {featuredImage && (
        <FeaturedImage
          src={featuredImage.src}
          alt={featuredImage.alt}
          caption={featuredImage.caption}
          credit={featuredImage.credit}
          priority={true}  // Hero images load immediately
        />
      )}
    </header>
  );
}
```

---

## 3. Integration with MDX

### Content Layer Integration

```typescript
// lib/content.ts - enhance existing content loader

interface Article {
  // ... existing fields
  featuredImage?: {
    src: string;
    alt: string;
    caption?: string;
    credit?: string;
  };
}

export async function getArticle(slug: string): Promise<Article> {
  const { frontmatter } = await parseMDX(slug);
  
  return {
    // ... existing fields
    featuredImage: frontmatter.featuredImage || null,
  };
}
```

### Page Template Update

```typescript
// app/blog/[slug]/page.tsx

import { ArticleHeader } from '@/components/ArticleHeader';

export default async function ArticlePage({ params }: { params: { slug: string } }) {
  const article = await getArticle(params.slug);
  
  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      <ArticleHeader
        title={article.title}
        description={article.description}
        featuredImage={article.featuredImage}
        category={article.category}
        readingTime={article.readingTime}
      />
      <div className="prose prose-lg max-w-none">
        {article.content}
      </div>
    </article>
  );
}
```

---

## 4. Image Optimization Pipeline

### next.config.js Settings

```javascript
// next.config.js
module.exports = {
  images: {
    formats: ['image/webp', 'image/jpeg'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    minimumCacheTTL: 60,
  },
};
```

### Script: Batch Image Optimization

```bash
#!/bin/bash
# scripts/optimize-images.sh

# Optimize all images in public/images
for img in public/images/*.{jpg,jpeg,png}; do
  if [ -f "$img" ]; then
    # Create WebP version
    cwebp -q 80 "$img" -o "${img%.*}.webp"
    
    # Create responsive sizes
    convert "$img" -resize 640x "${img%.*}-640.jpg"
    convert "$img" -resize 1024x "${img%.*}-1024.jpg"
    convert "$img" -resize 1920x "${img%.*}-1920.jpg"
  fi
done

echo "Image optimization complete"
```

---

## 5. Unsplash API Integration (Optional Enhancement)

### UnsplashService.ts

```typescript
// lib/unsplash.ts

const UNSPLASH_ACCESS_KEY = process.env.UNSPLASH_ACCESS_KEY;

interface UnsplashPhoto {
  id: string;
  urls: {
    raw: string;
    full: string;
    regular: string;
    small: string;
    thumb: string;
  };
  alt_description: string;
  user: {
    name: string;
    username: string;
  };
}

export async function searchUnsplash(
  query: string,
  count: number = 1
): Promise<UnsplashPhoto[]> {
  const response = await fetch(
    `https://api.unsplash.com/search/photos?query=${encodeURIComponent(query)}&per_page=${count}`,
    {
      headers: {
        Authorization: `Client-ID ${UNSPLASH_ACCESS_KEY}`,
      },
    }
  );
  
  const data = await response.json();
  return data.results;
}

// Usage in content workflow
export function generateUnsplashAttribution(photo: UnsplashPhoto): string {
  return `Photo by <a href="https://unsplash.com/@${photo.user.username}?utm_source=your_site&utm_medium=referral">${photo.user.name}</a> on <a href="https://unsplash.com/?utm_source=your_site&utm_medium=referral">Unsplash</a>`;
}
```

---

## 6. Content Workflow Integration

### Template Snippet for Writers

```markdown
---
title: "Article Title"
description: "SEO description"
featuredImage:
  src: "/images/article-category-keyword.jpg"
  alt: "Descriptive text for accessibility and SEO"
  credit: "Unsplash"
  photographer: "Photographer Name"
---

# Article Content
```

### Validation Script

```typescript
// scripts/validate-images.ts

import { glob } from 'glob';
import { parseMDX } from '../lib/content';

async function validateImages() {
  const files = await glob('content/**/*.mdx');
  const errors: string[] = [];
  
  for (const file of files) {
    const { frontmatter } = await parseMDX(file);
    
    if (!frontmatter.featuredImage) {
      errors.push(`${file}: Missing featuredImage`);
    } else {
      if (!frontmatter.featuredImage.src) {
        errors.push(`${file}: Missing featuredImage.src`);
      }
      if (!frontmatter.featuredImage.alt) {
        errors.push(`${file}: Missing featuredImage.alt`);
      }
      
      // Check if image file exists
      const fs = await import('fs');
      const imagePath = `public${frontmatter.featuredImage.src}`;
      if (!fs.existsSync(imagePath)) {
        errors.push(`${file}: Image not found: ${frontmatter.featuredImage.src}`);
      }
    }
  }
  
  if (errors.length > 0) {
    console.error('Image validation errors:');
    errors.forEach(e => console.error(`  - ${e}`));
    process.exit(1);
  } else {
    console.log('✓ All images validated successfully');
  }
}

validateImages();
```

---

## 7. Styling Guidelines

### Tailwind Classes for Featured Images

```css
/* Featured image container */
.featured-image {
  @apply relative w-full overflow-hidden rounded-lg;
  aspect-ratio: 16 / 9;
}

/* Image itself */
.featured-image img {
  @apply w-full h-full object-cover;
  transition: transform 0.3s ease;
}

/* Hover effect (optional) */
.featured-image:hover img {
  transform: scale(1.02);
}

/* Caption styling */
.featured-image figcaption {
  @apply text-sm text-gray-500 mt-2 text-center;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .featured-image {
    aspect-ratio: 4 / 3;
  }
}
```

---

## 8. Implementation Priority

### Week 1: Infrastructure
- [ ] Add FeaturedImage component
- [ ] Add ArticleHeader component
- [ ] Update content parsing to handle featuredImage
- [ ] Update article page templates
- [ ] Add image optimization script

### Week 2: Content Migration
- [ ] Retrofit existing articles with featured images
- [ ] Download/source images for top 20 articles per site
- [ ] Validate all images present
- [ ] Test responsive behavior

### Week 3: Enhancement
- [ ] Add Unsplash API integration (optional)
- [ ] Implement lazy loading for below-fold images
- [ ] Add image CDN integration (Cloudinary/Cloudflare)
- [ ] Create image management documentation

---

## 9. Site-Specific Image Strategies

### MaleOptimal
- **Style:** Active, confident men 40-60
- **Colors:** Warm, energetic
- **Subjects:** Gym, healthy food, consultation

### FuelOptimal
- **Style:** Food photography, overhead shots
- **Colors:** Natural, appetizing
- **Subjects:** Cooking process, finished dishes, ingredients

### GLP1Guide
- **Style:** Medical, clean, trustworthy
- **Colors:** Clinical blues, whites
- **Subjects:** Consultations, healthy portions, progress (not before/after)

### AIByRole
- **Style:** Modern, professional
- **Colors:** Tech-forward blues, greys
- **Subjects:** Home offices, collaboration, productivity

### LiftLab
- **Style:** Action-oriented, powerful
- **Colors:** Bold, high contrast
- **Subjects:** Weight training, gym equipment, strength

### TradePick
- **Style:** Professional, skilled
- **Colors:** Worksite earth tones
- **Subjects:** Tools in use, professional tradespeople

### RemotePivot
- **Style:** Lifestyle, flexible
- **Colors:** Natural, location-diverse
- **Subjects:** Remote work setups, coffee shops, coworking

---

## 10. Testing Checklist

- [ ] Images load correctly on all article pages
- [ ] Responsive images work (different sizes served)
- [ ] Alt text is present and descriptive
- [ ] Lazy loading works for below-fold images
- [ ] WebP format served with JPEG fallback
- [ ] No layout shift (CLS) on image load
- [ ] Attribution displays correctly
- [ ] Images are optimized (< 500KB each)
- [ ] CDN delivery working (if implemented)

---

*Infrastructure spec complete. Ready for implementation.*
