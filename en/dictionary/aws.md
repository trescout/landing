# What is Amazon Web Services?

*Dictionary · Dev · Last updated: September 22, 2026*

> Amazon Web Services

AWS (Amazon Web Services) is a cloud platform where you rent computing services such as servers, storage, and databases over the internet.

## Definition and Word Origin

Instead of setting up your own physical server, you rent Amazon data centers. Capacity grows when demand increases and shrinks when the work is done. It operates on a pay-as-you-go model. Almost all modern applications have this type of cloud infrastructure in the background.

***Analogy:** It's like buying electricity from the grid instead of building your own power plant; You only pay for what you use.*

## How to Know and Use in Daily Life?

**Website:** Servers that scale based on traffic.
**Backup:** A file vault that seems limitless.
**Video:** Content distributed as it is watched.
**Startup:** Go live without setting up a server room.

## Technical Depth and Architecture

Core services:

**EC2:** Virtual private server for rent.
**S3:** Object storage, backup and static file vault.
**RDS:** Managed relational database.
**Lambda:** Serverless function that runs on events.

Concepts:

**Region and availability zone:** Physical location and redundancy of data.
**Shared responsibility:** Security of the cloud is Amazon's responsibility, security of the data inside is yours.
**Free tier:** Limited free usage for new accounts.

To list running servers:

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

It is recommended to set a budget alarm to avoid billing surprises, as resources left running continue to incur charges.

## Frequently Mixed Things

It is often thought to be just a site hosting service. However, it is a complete infrastructure platform covering database, artificial intelligence, network, and security layers with over 200 services.

## Use in Different Disciplines

**Electrical network:** Unplugging instead of setting up a switchboard.
**Rental storage:** Renting as many shelves as needed.
**Taxi:** Traveling without owning a vehicle.

## Frequently Asked Questions

**Why should I use AWS?**

You gain instant access to enterprise infrastructure without making hardware investments. If traffic is volatile, scaling and ready-to-use services save time.

**Can I start for free?**

Yes. The free plan, credit, and duration conditions for new accounts may change over time; you should check the current limits on the AWS Free Tier page before starting.

**Where is my data stored?**

It is kept in the region you select. For regulations such as KVKK, you need to make your region selection and encryption according to your policy.

**How is the invoice kept under control?**

With budget alarms, cleanup of unused resources, and right-sizing. Tagging discipline is essential for small teams.

## Related terms

- [Cloud Computing](https://trescout.com/en/dictionary/cloud-computing/)
- [IaaS](https://trescout.com/en/dictionary/iaas/)
- [PaaS](https://trescout.com/en/dictionary/paas/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/aws/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/aws/
