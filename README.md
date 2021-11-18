# Hadoop-MapReduce-GCP

A Hadoop MapReduce application deployed on GCP to find the maximum temperature in every day of the years 1901 and 1902 from the NCDC weather records.

<br>

---

<br>

## Steps:

[UI Operations: 1 - 9]

[CLI Operations: 10 - 15 (commands are in screenshots)]

1. Login to GCP.
2. Enable billing on the working project.
3. Navigate to **Dataproc -> Clusters.**
4. Select the staging bucket attached to the cluster.
5. Upload the `mapper.py` , `reducer.py` and the data folder to the bucket.
6. Navigate into the cluster in Dataproc.
7. Select a **VM Instance**.
8. Use **SSH** of the virtual machine to interact.
9. Click **open in a new browser** in the **SSH** drop-down list.
10. Copy file and data from the bucket to the working directory on the cluster.
11. Put data on HDFS.
12. Do MapReduce.
13. Merge result files.
14. Copy the merged result file from cluster back to the bucket.
15. Download the result file from bucket.
