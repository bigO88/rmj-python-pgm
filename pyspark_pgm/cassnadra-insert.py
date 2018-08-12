from cassandra.cluster import Cluster
import pyspark as ps


cluster = Cluster()
session = cluster.connect('rmj_test')


result = session.execute("select * from emp")
for i in result:
    print(i.emp_id,i.emp_name)





