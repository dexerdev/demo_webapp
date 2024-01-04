class api_result:
    def __init__(self,data=None,success=False,message='',error=None) :
        self.data=data
        self.success=success
        self.message=message
