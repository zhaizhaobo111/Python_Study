# store基本操作
import uuid

from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.postgres import PostgresStore

DB_URI="postgresql://postgres:bit@localhost:5432/postgres"
with (
    PostgresSaver.from_conn_string(DB_URI) as checkpointer,
    PostgresStore.from_conn_string(DB_URI) as store,
):
    # 第一次创建表
    # store.setup()
    user_id="user_111"
    namespace=(user_id,"preference","food")
    memory_id=str(uuid.uuid4())
    memory_value={"melon":"watermelon"}
    store.put(namespace=namespace,key=memory_id,value=memory_value)
    print(store.get(namespace,memory_id))
