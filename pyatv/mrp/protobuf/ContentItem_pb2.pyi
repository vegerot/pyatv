# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.ContentItemMetadata_pb2 import (
    ContentItemMetadata as pyatv___mrp___protobuf___ContentItemMetadata_pb2___ContentItemMetadata,
)

from pyatv.mrp.protobuf.LanguageOption_pb2 import (
    LanguageOption as pyatv___mrp___protobuf___LanguageOption_pb2___LanguageOption,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ContentItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    identifier = ... # type: typing___Text
    info = ... # type: typing___Text
    parentIdentifier = ... # type: typing___Text
    ancestorIdentifier = ... # type: typing___Text
    queueIdentifier = ... # type: typing___Text
    requestIdentifier = ... # type: typing___Text

    @property
    def metadata(self) -> pyatv___mrp___protobuf___ContentItemMetadata_pb2___ContentItemMetadata: ...

    @property
    def availableLanguageOptions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pyatv___mrp___protobuf___LanguageOption_pb2___LanguageOption]: ...

    @property
    def currentLanguageOptions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pyatv___mrp___protobuf___LanguageOption_pb2___LanguageOption]: ...

    def __init__(self,
        *,
        identifier : typing___Optional[typing___Text] = None,
        metadata : typing___Optional[pyatv___mrp___protobuf___ContentItemMetadata_pb2___ContentItemMetadata] = None,
        info : typing___Optional[typing___Text] = None,
        availableLanguageOptions : typing___Optional[typing___Iterable[pyatv___mrp___protobuf___LanguageOption_pb2___LanguageOption]] = None,
        currentLanguageOptions : typing___Optional[typing___Iterable[pyatv___mrp___protobuf___LanguageOption_pb2___LanguageOption]] = None,
        parentIdentifier : typing___Optional[typing___Text] = None,
        ancestorIdentifier : typing___Optional[typing___Text] = None,
        queueIdentifier : typing___Optional[typing___Text] = None,
        requestIdentifier : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContentItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ancestorIdentifier",u"identifier",u"info",u"metadata",u"parentIdentifier",u"queueIdentifier",u"requestIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ancestorIdentifier",u"availableLanguageOptions",u"currentLanguageOptions",u"identifier",u"info",u"metadata",u"parentIdentifier",u"queueIdentifier",u"requestIdentifier"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ancestorIdentifier",b"ancestorIdentifier",u"identifier",b"identifier",u"info",b"info",u"metadata",b"metadata",u"parentIdentifier",b"parentIdentifier",u"queueIdentifier",b"queueIdentifier",u"requestIdentifier",b"requestIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ancestorIdentifier",b"ancestorIdentifier",u"availableLanguageOptions",b"availableLanguageOptions",u"currentLanguageOptions",b"currentLanguageOptions",u"identifier",b"identifier",u"info",b"info",u"metadata",b"metadata",u"parentIdentifier",b"parentIdentifier",u"queueIdentifier",b"queueIdentifier",u"requestIdentifier",b"requestIdentifier"]) -> None: ...
