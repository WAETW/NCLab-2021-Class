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
        Switch = self.addSwitch( 's1' )


        # Add links
        self.addLink( leftHost_1, Switch )
        self.addLink( leftHost_2, Switch )
        self.addLink( Switch, rightHost_1 )
        self.addLink( Switch, rightHost_2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }