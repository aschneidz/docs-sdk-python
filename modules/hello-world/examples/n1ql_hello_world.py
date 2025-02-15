from couchbase.cluster import Cluster, PasswordAuthenticator
from couchbase.exceptions import CouchbaseException

cluster = Cluster("couchbase://localhost",
                  authenticator=PasswordAuthenticator("Administrator", "password"))

try:
    # tag::n1ql-query[]
    # Call the query() function on the cluster object and store the result.
    result = cluster.query("SELECT \"Hello World\" as greeting")

    # Iterate over the rows to access result data and print to the terminal.
    for row in result.rows():
        print(row)
    # end::n1ql-query[]
except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
