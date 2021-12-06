# Pull Clickhouse Server
docker pull yandex/clickhouse-server


# Run Click house Server
docker run -d --name some-clickhouse-server --ulimit nofile=262144:262144 yandex/clickhouse-server


# Connect to Clickhouse
docker run -it --rm --link some-clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server

## Create database
```
CREATE DATABASE IF NOT EXISTS geo
```

## Create database

```
CREATE TABLE geo.modc4
(
    `Band` String,
    `EventTime` DateTime,
    `EventDate` Date,
    `Row` Int8,
    `Column` Int8,
    `Data` Float64
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(EventDate)
ORDER BY (Row)
```