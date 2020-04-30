# quickstart-nvidia-imaging-clara-train
## NVIDIA Clara Train SDK for Medical Imaging on the AWS Cloud

This Quick Start deploys the Clara Train SDK as a highly available service, based on Amazon Elastic Container Service (Amazon ECS).

The [NVIDIA Clara Train SDK](https://docs.nvidia.com/clara/) provides an AI Assisted Annotation developer toolkit that can be integrated into existing Medical Viewers, accelerating the creation of AI-ready, annotated medical imaging datasets. Clara Train also provides a TensorFlow based training framework with domain-specific pre-trained models that accelerate AI development with techniques like Transfer Learning, Federated Learning, and AutoML. Models trained with Clara Train are packaged as Medical Model Archives (MMARs) providing a standardized format for training workflows and collaborations.

This Quick Start offers two deployment options:

- Deploying NVIDIA Clara Train SDK into a new virtual private cloud (VPC) on AWS
- Deploying NVIDIA Clara Train SDK into an existing VPC on AWS

You can also use the AWS CloudFormation templates as a starting point for your own implementation.

![Quick Start architecture for NVIDIA Clara Train SDK on AWS](https://d1.awsstatic.com/partner-network/QuickStart/datasheets/nvidia-clara-train-sdk-architecture-diagram.454bcb343ee0cc4e73e3a85a39ec236fcbab54b2.png)

After the CloudFormation templates have been deployed, the [stack outputs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) contain a link to the load-balanced URL for the AI-Assisted Annotation APIs and Annotation Server, and the DNS name of the Amazon Elastic File System (Amazon EFS).

The command line Clara SDK tools can be used by SSH, via the bastion host, to the ECS host. Then, open a shell to the Clara container running on the ECS host.

For architectural details, best practices, step-by-step instructions, and customization options, see the 
[deployment guide](https://aws-quickstart.s3.amazonaws.com/quickstart-nvidia-clara-medical-imaging/doc/nvidia-clara-medical-imaging-on-the-aws-cloud.pdf).

To post feedback, submit feature ideas, or report bugs, use the **Issues** section of this GitHub repo.
If you'd like to submit code for this Quick Start, please review the [AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
