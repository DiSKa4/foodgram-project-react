class ReprMixin(object):
    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return self.serializer(instance.recipe, context=context).data
