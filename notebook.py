

class Notebook:
    """Notebook class inherited from Computer and Monitor

    has constructor
    """
    def __init__( ) -> None:
        """constructor of notebook 


        calls computer and monitor init methods with self

        sets the price of notebook 
        Args:
            brand (_type_): brand of Notebook
            price (_type_): price  of Notebook
            cpu (_type_): cpu of Notebook
            ram (_type_): ram of Notebook
            disk (_type_): disk of Notebook
            gpu (_type_): gpu of Notebook
            monitor_size (_type_): monitor size  of Notebook
            monitor_type (str, optional): monitor type of notebook . Defaults to "integrated".
        """ 
