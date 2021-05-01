from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost_1 = self.addHost( 'h1' )
        leftHost_2 = self.addHost( 'h2' )
        rightHost_1 = self.addHost( 'h3' )
        rightHost_2 = self.addHost( 'h4' )
        Switch_1 = self.addSwitch( 's1' )
        Switch_2 = self.addSwitch( 's2' )
        Switch_3 = self.addSwitch( 's3' )
        Switch_4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost_1, Switch_1 )
        self.addLink( leftHost_2, Switch_1 )
        self.addLink( Switch_1, Switch_2 )
        self.addLink( Switch_1, Switch_3 )
        self.addLink( Switch_2, Switch_4 )
        self.addLink( Switch_3, Switch_4 )
        self.addLink( Switch_4, rightHost_1 )
        self.addLink( Switch_4, rightHost_2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }