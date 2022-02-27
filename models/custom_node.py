from graphene.relay import Node


class CustomNode(Node):
    """
    Fixing Graphene weird ID style
    """

    class Meta:
        name = 'pokeNode'

    @staticmethod
    def to_global_id(type, id, **kwargs):  # noqa
        return id
