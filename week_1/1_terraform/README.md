

### Project infrastructure:
 * Google Cloud Storage (GSC): Data Lake
 * BigQuery: DWH 

### Setup Access
1. IAM Roles for Service account(go to console -> IAM -> add roles):
    * Storage admin: to create buckets and create files (granting our service to do that)
    * Storage Object Admin: to do soething with objects (DML/DDL)
    * BigQuery Admin: to interact with BigQuery
2. Enable these APIs for your project:
   *
3. GOOGLE_APPLICATION_CREDENTIALS env-var have to be set up
```aidl
export GOOGLE_APPLICATION_CREDENTIALS = "/home/vsvld/Projects/dataEngZoomcamp/week_1/2_docker_sql/dtc.json"
```
4.Execution 
```aidl
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"

# Create new infra
terraform apply -var="project=<your-gcp-project-id>"

# Delete infra after your work, to avoid costs on any running services
terraform destroy
```