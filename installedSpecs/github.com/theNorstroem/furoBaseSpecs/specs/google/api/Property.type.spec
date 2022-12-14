name: Property
type: Property
description: |-
    Defines project properties.

     API services can define properties that can be assigned to consumer projects
     so that backends can perform response customization without having to make
     additional calls or maintain additional storage. For example, Maps API
     defines properties that controls map tile cache period, or whether to embed a
     watermark in a result.

     These values can be set via API producer console. Only API providers can
     define and set these properties.
lifecycle: null
__proto:
    package: google.api
    targetfile: consumer.proto
    imports:
        - google/api/Property/ENUM_consumer.proto
    options:
        go_package: google.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig
        java_multiple_files: "true"
        java_outer_classname: ConsumerProto
        java_package: com.google.api
fields:
    name:
        type: string
        description: The name of the property (a.k.a key).
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: label.Property.name
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    type:
        type: google.api.Property.PropertyType
        description: The type of this property.
        __proto:
            number: 2
        __ui: null
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: label.Property.type
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    description:
        type: string
        description: The description of the property
        __proto:
            number: 3
        __ui: null
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: label.Property.description
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
