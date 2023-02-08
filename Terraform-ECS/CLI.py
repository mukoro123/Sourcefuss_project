import argparse
import boto3

def list_files_in_s3_bucket(sourcefuss-nginx-bucket):
    s3 = boto3.client("s3")
    result = s3.list_objects(Bucket=sourcefuss-nginx-bucket)
    if "Contents" in result:
        for obj in result["Contents"]:
            print(obj["Key"])
    else:
        print("No files found in bucket '{}'".format(sourcefuss-nginx-bucket))

def list_task_definition_versions(test-def):
    ecs = boto3.client("ecs")
    result = ecs.list_task_definition_families(status="ACTIVE")
    if "test-def" in result["families"]:
        result = ecs.list_task_definitions(familyPrefix="test-def", sort="DESC")
        for task_definition in result["taskDefinitionArns"]:
            print(task_definition)
    else:
        print("Task definition '{}' not found".format("test-def"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The command to run (list-files-in-s3-bucket or list-task-definition-versions)")
    parser.add_argument("--sourcefuss-nginx-bucket", help="The name of the S3 bucket")
    parser.add_argument("--test-def", help="The name of the ECS task definition")
    args = parser.parse_args()

    if args.command == "list-files-in-s3-bucket":
        list_files_in_s3_bucket(args.sourcefuss-nginx-bucket)
    elif args.command == "list-task-definition-versions":
        list_task_definition_versions(args."test-def")
    else:
        print("Unknown command '{}'".format(args.command))

   ######  Here is an example implementation of the CLI in Python using the AWS SDK (boto3) to interact with S3 and ECS
   ######  Note: You must have the AWS CLI installed and configured, and have sufficient permissions to access the desired S3 bucket and ECS task definition.

