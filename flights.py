

    # Load the airlines data set with  airline names and codes. Note because of lazy loading, airlines is still a reference to abase dataset.
    # A new dataset isn't loaded in memory yet. Dataset will be loaded only when an action is performed by a worker.
         airlines = sc.textFile("/usr/local/spark-2.2.1-bin-hadoop2.7/bin/data/airlines.csv")
         print (airlines.take(3))
   #    print (airlines.first())

    #Transform the RDD into a dictionary
     #  airlines.map(split).collect()


   #for x in airlines.collect():
    #    print x

    #counts = airlines.count()
    #print "The obj in RDD", counts

    #Boradcast the airlines RDD across the cluster
    #sc.broadcast(airlines)






    if __name__ == "__main__":
     # Configure Spark
     conf = SparkConf().setAppName(APP_NAME)
     conf = conf.setMaster("local[*]")
     sc   = SparkContext(conf=conf)

    # Execute Main functionality
     main(sc)
                                                                                                             66,0-1        Bot
