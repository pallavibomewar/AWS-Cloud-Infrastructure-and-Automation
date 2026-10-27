# AWS S3 Static Website Hosting
# Project Overview
I created and hosted a simple static website using Amazon S3.

# Tools Used
   AWS S3
   HTML
   AWS Management Console
# Steps Performed
   Created an S3 bucket.
   Created an HTML file named index.html.
   Uploaded the HTML file to the S3 bucket.
   Enabled static website hosting.
   Set index.html as the index document.
   Opened the website endpoint and verified that the website was working.
# Result
  Successfully hosted my first static website using Amazon S3.

# Website URL
http://pallavi-cloud-site-261026.s3-website.eu-north-1.amazonaws.com

## Amazon CloudFront CDN Integration

I deployed a static website using Amazon S3 and integrated Amazon CloudFront for content delivery.

### Deployment Steps
1. Created an Amazon S3 bucket.
2. Uploaded the `index.html` file.
3. Configured S3 static website hosting and tested the website.
4. Created an Amazon CloudFront distribution.
5. Selected the existing S3 bucket as the origin.
6. Enabled Origin Access Control (OAC) for private S3 bucket access.
7. Configured the S3 bucket policy to allow CloudFront access.
8. Set `index.html` as the default root object.
9. Tested the CloudFront URL successfully.

### Live Website URL
https://d2bgxs7hzm1tam.cloudfront.net/

### Security
Used CloudFront Origin Access Control (OAC) to access the S3 bucket securely without requiring public bucket access.
