# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install --production

# Final stage
FROM node:18-alpine
WORKDIR /app

# Create non-root user
RUN adduser -D appuser

COPY --from=builder /app/node_modules ./node_modules
COPY app.js .
COPY views/ ./views/

RUN chown -R appuser:appuser /app
USER appuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:3000 || exit 1

EXPOSE 3000
CMD ["node", "app.js"]
