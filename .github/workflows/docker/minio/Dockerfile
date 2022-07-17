FROM minio/minio:latest
RUN mkdir -p /data/.minio.sys/buckets
ENTRYPOINT ["minio"]
CMD ["server ."]