Shopify Centralized Database Project

This project is a centralized inventory management system built to serve as an internal tool for syncing and organizing data from a Shopify store. It is designed to eventually become a stand-alone solution for small e-commerce vendors to easily manage their product catalogs, orders, and customers across platforms.

🎯 Purpose 
- Streamline and centralize Shopify store data
- Enable multi-platform support (e.g., Amazon, Etsy, TikTok Shop)	
- Build a scalable backend using AWS serverless infrastructure
- Feed clean data to a frontend for internal use
- Notify stakeholders of database/API activity through alerts
- Keep the tool simple, clear, and easy to use


🛠 Tech Stack 
- Backend: Python
- Database: Amazon RDS (PostgreSQL)
- Cloud Services:
  - AWS EventBridge – receives Shopify webhooks
  - AWS Lambda – processes events and writes to RDS
  - AWS SNS – sends out notifications for DB/API activity
  - AWS SQS (optional) – queueing for async processing or retries
  - AWS API Gateway – serves data to frontend
  - Amazon S3 – frontend access to exposed data
- Shopify API: Admin REST or GraphQL


🔄 Key Features
- Automatically syncs Shopify products, orders, and customers
- Serverless, event-driven backend
- Centralized PostgreSQL inventory database
- API + S3 feed for internal dashboards
- Notification system for DB/API changes via SNS


🚀 Quick Start
1. Clone the Repo
2. Set Up Secrets 
   - Use environment variables or AWS Secrets Manager for:
     - Shopify Admin API credentials
     - PostgreSQL credentials
3. Connect Shopify to AWS EventBridge
   - Register Shopify as a partner EventBridge source
   - Subscribe to webhook topics like:
     - products/create, products/update
     - orders/create
     - customers/create
4. Deploy AWS Lambda Functions
   - Webhook Handler (triggered by EventBridge)
   - SNS Notification Publisher (triggers on DB/API activity) 
   - API Gateway Handler (serves data to S3)
   - Optional: Add SQS if needed for buffering or retries.
5. Set Up PostgreSQL
   - Run the schema in sql/schema.sql to set up your database.
6. Connect Frontend
   - Use API Gateway and S3 to expose curated data for internal dashboards or co-worker use.


📣 Notifications 
- This project uses AWS SNS to send alerts or status updates on:
  - Database insert/update events
  - API fetch operations
  - Sync errors or retries 
  - Recipients can subscribe via email, SMS, or HTTP endpoint.


🧭 Roadmap 
- Build dashboard UI (optional) 
- Add multi-store support (Amazon, Etsy)
- Advanced data validation and syncing integrity
- CLI/installer for new store onboarding


👥 Who Is This For? 
- Shopify sellers scaling beyond built-in tools
- Fulfillment partners managing multiple vendors
- Internal team members needing clean inventory data
- Developers building low-maintenance inventory infrastructure