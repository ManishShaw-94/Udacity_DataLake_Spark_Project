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

# Script generated for node Customer Privacy Join
CustomerPrivacyJoin_node2 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1678630816695,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="CustomerPrivacyJoin_node2",
)

# Script generated for node Drop Fields
DropFields_node1678631456241 = DropFields.apply(
    frame=CustomerPrivacyJoin_node2,
    paths=[
        "serialNumber",
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="DropFields_node1678631456241",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1678631456241,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://manish-s3-lake-house/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
