from pyspark import SparkConf,SparkContext


conf = SparkConf().setAppName('Test11').setMaster('local')
sc = SparkContext(conf=conf)
data = [1, 2, 3, 4]

distData = sc.parallelize(data)

distData.foreach(lambda x: print(x))

rdd = sc.textFile('/home/rajjanwa/PycharmProjects/rajdemo/pyspark_pgm/SparkPgm.py')

rdd.foreach(lambda x: print(x))


