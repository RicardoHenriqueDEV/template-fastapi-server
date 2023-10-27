from fastapi import APIRouter
from controllers.main import publicRoute, healthCheck, handleSum

main_routes = APIRouter()

main_routes.add_api_route("/", endpoint=publicRoute, methods=["GET"])
main_routes.add_api_route("/health", endpoint=healthCheck, methods=["GET"])
main_routes.add_api_route("/sum", endpoint=handleSum, methods=["POST"])