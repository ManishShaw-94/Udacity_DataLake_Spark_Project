import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://manish-s3-lake-house/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Amazon S3
AmazonS3_node1678630816695 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://manish-s3-lake-house/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1678630816695",
)

# Script generated for node Amazon S3
AmazonS3_node1678712397112 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://manish-s3-lake-house/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1678712397112",
)

# Script generated for node Customer Privacy Join
CustomerPrivacyJoin_node2 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1678630816695,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="CustomerPrivacyJoin_node2",
)

# Script generated for node StepTrainerAccelerometerCustomer Privacy Join
StepTrainerAccelerometerCustomerPrivacyJoin_node1678712668552 = Join.apply(
    frame1=CustomerPrivacyJoin_node2,
    frame2=AmazonS3_node1678712397112,
    keys1=["serialNumber", "timeStamp"],
    keys2=["serialNumber", "sensorReadingTime"],
    transformation_ctx="StepTrainerAccelerometerCustomerPrivacyJoin_node1678712668552",
)

# Script generated for node Drop Fields
DropFields_node1678631456241 = DropFields.apply(
    frame=StepTrainerAccelerometerCustomerPrivacyJoin_node1678712668552,
    paths=[
        "shareWithFriendsAsOfDate",
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "sensorReadingTime",
    ],
    transformation_ctx="DropFields_node1678631456241",
)

# Script generated for node MachineLearningCurated
MachineLearningCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1678631456241,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://manish-s3-lake-house/machine_learning/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="MachineLearningCurated_node3",
)

job.commit()
