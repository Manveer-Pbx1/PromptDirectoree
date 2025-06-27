from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from datetime import datetime

from rest_framework.views import APIView

from .serializers import PromptSerializer
from .database.mongodb import prompts_collection, serialize_prompt

class PromptListCreateView(APIView):
    def get(self, request):
        prompts = prompts_collection.find().sort("created_at", -1)
        serialized = [serialize_prompt(p) for p in prompts]
        return Response(serialized)

    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            now = datetime.now()
            result = prompts_collection.insert_one({
                "title": data["title"],
                "content": data["content"],
                "created_at": now,
                "updated_at": now,
            })
            prompt = prompts_collection.find_one({"_id": result.inserted_id})
            return Response(serialize_prompt(prompt), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PromptDetailsView(APIView):
    def get_object(self, id):
        try:
            return prompts_collection.find_one({"_id": ObjectId(id)})
        except:
            return None

    def get(self, request, id):
        prompt = self.get_object(id)
        if not prompt:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialize_prompt(prompt), status=status.HTTP_200_OK)

    def put(self, request, id):
        prompt = self.get_object(id)
        if not prompt:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            updated = {
                "title": data["title"],
                "content": data["content"],
                "updated_at": datetime.now()
            }
            prompts_collection.update_one({"_id": ObjectId(id)}, {"$set": updated})
            prompt = prompts_collection.find_one({"_id": ObjectId(id)})
            return Response(serialize_prompt(prompt), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = prompts_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Successfully deleted prompt"}, status=status.HTTP_204_NO_CONTENT)