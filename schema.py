#dannie  2018/9/18  11:20  PyCharm
import graphene

class Query(graphene.ObjectType):
    hello=graphene.String()

    def resolve_hello(self,info):
        return 'aiohttp'

schema=graphene.Schema(query=Query)

