The following the annotated output of running ./TestClientFunctions.sh in the /test folder.  Make sure the 3-tier servers are up and running, this can be done quickly by running the following command from the src folder:

    ./server_startup.sh [edlab ssh username]
    
For each time, we test buy and lookup.  Buy is called 5 times, with the initial stock varying from 6 to 3.  Lookup is called after buying 5 times, to ensure the remaining stock is max(0,initial - 5)

    Buying first item 5 times, starting at stock 6
    {"How to get a good grade in 677 in 20 minutes a day":{"COST":120.0,"QUANTITY":6}}
    bought book 'How to get a good grade in 677 in 20 minutes a day'

    bought book 'How to get a good grade in 677 in 20 minutes a day'

    bought book 'How to get a good grade in 677 in 20 minutes a day'

    bought book 'How to get a good grade in 677 in 20 minutes a day'

    bought book 'How to get a good grade in 677 in 20 minutes a day'

    Looking up final stock of first item
    Name: How to get a good grade in 677 in 20 minutes a day
    Cost: 120.0
    Quantity: 1

    Buying second item 5 times, starting at stock 5
    {"RPCs for Dummies":{"COST":160.0,"QUANTITY":5}}
    bought book 'RPCs for Dummies'

    bought book 'RPCs for Dummies'

    bought book 'RPCs for Dummies'

    bought book 'RPCs for Dummies'

    bought book 'RPCs for Dummies'

    Looking up final stock of second item
    Name: RPCs for Dummies
    Cost: 160.0
    Quantity: 0

Starting at 4 items, we should starting seeing failed buy operations.  In this case, the last buy should be a fail.
    Buying third item 5 times, starting at stock 4
    {"Xen and the Art of Surviving Graduate School":{"COST":150.0,"QUANTITY":4}}
    bought book 'Xen and the Art of Surviving Graduate School'

    bought book 'Xen and the Art of Surviving Graduate School'

    bought book 'Xen and the Art of Surviving Graduate School'

    bought book 'Xen and the Art of Surviving Graduate School'

    failed to buy book 'Xen and the Art of Surviving Graduate School'

    Looking up final stock of third item
    Name: Xen and the Art of Surviving Graduate School
    Cost: 150.0
    Quantity: 0
    
There should be 2 fails for this one.

    Buying fourth item 5 times, starting at stock 3
    {"Cooking for the Impatient Graduate Student":{"COST":140.0,"QUANTITY":3}}
    bought book 'Cooking for the Impatient Graduate Student'

    bought book 'Cooking for the Impatient Graduate Student'

    bought book 'Cooking for the Impatient Graduate Student'

    failed to buy book 'Cooking for the Impatient Graduate Student'

    failed to buy book 'Cooking for the Impatient Graduate Student'

    Looking up final stock of fourth item
    Name: Cooking for the Impatient Graduate Student
    Cost: 140.0
    Quantity: 0

Finally, we test the search by topic function for both topics.

    Searching topic graduate_school
    Name: Xen and the Art of Surviving Graduate School Item ID: 3
    Name: Cooking for the Impatient Graduate Student Item ID: 4

    Searching topic distributed_systems
    Name: RPCs for Dummies Item ID: 2
    Name: How to get a good grade in 677 in 20 minutes a day Item ID: 1

    Done testing basic client operations!
