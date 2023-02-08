import boto3
import unittest

class TestECSCluster(unittest.TestCase):
    def setUp(self):
        self.ecs = boto3.client("ecs")

    def test_list_clusters(self):
        response = self.ecs.list_clusters()
        self.assertIn("clusterArns", response)

    def test_describe_cluster(self):
        response = self.ecs.list_clusters()
        if response["clusterArns"]:
            cluster_arn = response["clusterArns"][0]
            response = self.ecs.describe_clusters(clusters=[cluster_arn])
            self.assertIn("clusters", response)
            self.assertGreater(len(response["clusters"]), 0)
        else:
            self.fail("No clusters found")

if __name__ == "__main__":
    unittest.main()


####### You can run the tests by executing the script with python test_ecs_cluster.py
###### If a test fails, you will see output indicating which test failed and why.
####### This is a basic example, and you can extend the tests to cover more of the ECS API and validate more complex scenarios as needed.
