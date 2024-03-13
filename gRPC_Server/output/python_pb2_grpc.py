# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from messages.line import push_message_pb2 as messages_dot_line_dot_push__message__pb2


class GrpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LinePushMessage = channel.unary_unary(
                '/GrpcService/LinePushMessage',
                request_serializer=messages_dot_line_dot_push__message__pb2.LinePushMessageRequest.SerializeToString,
                response_deserializer=messages_dot_line_dot_push__message__pb2.LinePushMessageResponse.FromString,
                )


class GrpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LinePushMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LinePushMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.LinePushMessage,
                    request_deserializer=messages_dot_line_dot_push__message__pb2.LinePushMessageRequest.FromString,
                    response_serializer=messages_dot_line_dot_push__message__pb2.LinePushMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LinePushMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcService/LinePushMessage',
            messages_dot_line_dot_push__message__pb2.LinePushMessageRequest.SerializeToString,
            messages_dot_line_dot_push__message__pb2.LinePushMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
