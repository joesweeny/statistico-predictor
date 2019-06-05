# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from predictor.grpc.proto.prediction import prediction_pb2 as predictor_dot_grpc_dot_proto_dot_prediction_dot_prediction__pb2


class PredictionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOverUnderGoalsForFixture = channel.unary_unary(
        '/prediction.PredictionService/GetOverUnderGoalsForFixture',
        request_serializer=predictor_dot_grpc_dot_proto_dot_prediction_dot_prediction__pb2.OverUnderRequest.SerializeToString,
        response_deserializer=predictor_dot_grpc_dot_proto_dot_prediction_dot_prediction__pb2.OverUnderGoalsResponse.FromString,
        )


class PredictionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOverUnderGoalsForFixture(self, request, context):
    """Returns a Over/Under goals prediction for a given fixture
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOverUnderGoalsForFixture': grpc.unary_unary_rpc_method_handler(
          servicer.GetOverUnderGoalsForFixture,
          request_deserializer=predictor_dot_grpc_dot_proto_dot_prediction_dot_prediction__pb2.OverUnderRequest.FromString,
          response_serializer=predictor_dot_grpc_dot_proto_dot_prediction_dot_prediction__pb2.OverUnderGoalsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'prediction.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
