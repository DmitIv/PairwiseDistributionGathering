from data_gathering.clickhouse_agent.agent import ClickhouseQuery
from data_gathering.tarantool_agent.agent import TarantoolUpsert


class Flow:
    def __init__(self, clickhouse_side: ClickhouseQuery, tarantool_side: TarantoolUpsert):
        self.clickhouse = clickhouse_side
        self.tarantool = tarantool_side

    def prepare_clickhouse_query(self, **kwargs):
        self.clickhouse = self.clickhouse.prepare_query(**kwargs)
        return self

    async def start(self):
        await self.tarantool.upsert_from(self.clickhouse.execute())
