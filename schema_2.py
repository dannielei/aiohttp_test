#dannie  2018/9/20  8:43  PyCharm
import graphene
import pandas as pd

class Crew(graphene.ObjectType):
    name = graphene.String()
    value = graphene.String()

class Query(graphene.ObjectType):
    crew=graphene.Field(graphene.List(Crew))

    def resolve_crew(self, info):
        df = pd.DataFrame([['one', '1'], ['two', '2']], columns=['name', 'value'])
        rt=[]
        for i in df.index:
            f=Crew()
            f.name=df.loc[i].values[0]
            f.value=df.loc[i].values[1]
            rt.append(f)
        return rt

schema_2=graphene.Schema(query=Query)



