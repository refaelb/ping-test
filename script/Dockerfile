FROM debian:stretch
COPY test-ping.sh .
RUN chmod +x test-ping.sh
RUN apt-get update && apt-get install -y \
curl

# CMD ["/bin/sh", "test-ping.sh"]
CMD ["./test-ping.sh"]