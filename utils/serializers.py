from rest_framework import serializers


class CustomHyperLinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Adds an id(pk) field to the HyperlinkedModelSerializer
    """

    def get_default_field_names(self, declared_fields, model_info):
        """
        Return the default list of field names that will be used if the
        `Meta.fields` option is not specified.
        """
        return (
                [model_info.pk.name] +  # added this
                [self.url_field_name] +
                list(declared_fields) +
                list(model_info.fields) +
                list(model_info.forward_relations)
        )
