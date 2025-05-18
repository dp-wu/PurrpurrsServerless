# **Shopify Centralized Database Project**

This project is a centralized inventory management system designed to serve as an internal tool for syncing and organizing data from a Shopify store. It’s built to scale into a stand-alone backend solution for small e-commerce vendors to manage products, orders, and customers across platforms.

---

## 🎯 Purpose
- Streamline and centralize Shopify store data
- Support future multi-channel sync (e.g., Amazon, Etsy, TikTok Shop)
- Build a scalable, serverless backend using AWS infrastructure
- Feed clean and structured data to a frontend for internal operations
- Alert stakeholders on critical database/API activity
- Keep architecture simple, clear, and extendable

---

## 🛠 Tech Stack

- **Backend**: Python
- **Database**: PostgreSQL (Amazon RDS)
  - Hybrid schema: relational tables for core data + `JSONB` columns for flexible fields like Shopify product options
- **Cloud Infrastructure**:
  - AWS Lambda – core logic handler (webhooks, syncing, API responses)
  - AWS EventBridge – receives Shopify webhooks
  - AWS SNS – publishes alerts on DB/API activity
  - AWS SQS (optional) – buffers webhook payloads or retries failed ops
  - AWS API Gateway – internal API layer
  - Amazon S3 – serves exposed data to frontend apps

- **Shopify Integration**:
  - Shopify Admin API (REST or GraphQL)

---

## 🔄 Key Features

- Ingests Shopify product, order, and customer events via webhooks
- Uses JSONB fields to store flexible, semi-structured Shopify data
- Serverless backend (fully event-driven and low maintenance)
- Centralized PostgreSQL database with optional raw payload logging
- Notification system via SNS for inserts, updates, and errors
- Internal API and S3 support for dashboards or analyst access

---

## 🚀 Quick Start

1. **Clone the Repo**

2. **Set Up Environment Variables / Secrets**
   - Shopify API credentials
   - PostgreSQL connection URL
   - (Optional) AWS credentials for Lambda/S3 if not using IAM roles

3. **Connect Shopify to AWS EventBridge**
   - Register EventBridge as a partner destination
   - Subscribe to Shopify webhook topics:
     - `products/create`, `products/update`
     - `orders/create`
     - `customers/create`

4. **Deploy AWS Lambda Functions**
   - Webhook Processor (EventBridge → DB)
   - SNS Publisher (for alerts)
   - API Gateway Handler (fetches data from DB)
   - (Optional) SQS Handler for retryable workloads

5. **Set Up PostgreSQL**
   - Tables will be created via SQLAlchemy
   - JSONB fields store Shopify options/metafields flexibly

6. **Connect Frontend (Optional)**
   - Use API Gateway or expose snapshots to S3 for internal tools or dashboards

---

## 📣 Notifications

AWS SNS publishes alerts for:
- Successful inserts/updates
- API data fetches
- Sync or transformation errors
- Recipients: email, SMS, or webhook endpoints

---

## 🧭 Roadmap

- Add dashboard UI for product and order insights
- Multi-store (multi-Shopify or cross-platform) support
- Enhanced data validation and syncing logic
- CLI tool for onboarding new stores with minimal setup
- S3 snapshots for backup/versioning

---

## 👥 Who Is This For?

- Shopify sellers scaling beyond native admin tools
- Fulfillment centers handling inventory for multiple merchants
- Ops or data teams needing consistent, normalized store data
- Developers building a low-maintenance inventory pipeline