# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from .Chat import DefaultChatSettings


class Agent(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    metadata: dict[str, Any] | None = None
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """
    name: Annotated[
        str,
        Field(
            "",
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the agent
    """
    about: str = ""
    """
    About the agent
    """
    model: str = ""
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """
    instructions: str | list[str] = ""
    """
    Instructions for the agent
    """
    default_settings: DefaultChatSettings | None = None
    """
    Default settings for all sessions created by this agent
    """


class CreateAgentRequest(BaseModel):
    """
    Payload for creating a agent (and associated documents)
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    metadata: dict[str, Any] | None = None
    name: Annotated[
        str,
        Field(
            "",
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the agent
    """
    about: str = ""
    """
    About the agent
    """
    model: str = ""
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """
    instructions: str | list[str] = ""
    """
    Instructions for the agent
    """
    default_settings: DefaultChatSettings | None = None
    """
    Default settings for all sessions created by this agent
    """


class CreateOrUpdateAgentRequest(CreateAgentRequest):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: UUID
    metadata: dict[str, Any] | None = None
    name: Annotated[
        str,
        Field(
            "",
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the agent
    """
    about: str = ""
    """
    About the agent
    """
    model: str = ""
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """
    instructions: str | list[str] = ""
    """
    Instructions for the agent
    """
    default_settings: DefaultChatSettings | None = None
    """
    Default settings for all sessions created by this agent
    """


class PatchAgentRequest(BaseModel):
    """
    Payload for patching a agent
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    metadata: dict[str, Any] | None = None
    name: Annotated[
        str,
        Field(
            "",
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the agent
    """
    about: str = ""
    """
    About the agent
    """
    model: str = ""
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """
    instructions: str | list[str] = ""
    """
    Instructions for the agent
    """
    default_settings: DefaultChatSettings | None = None
    """
    Default settings for all sessions created by this agent
    """


class UpdateAgentRequest(BaseModel):
    """
    Payload for updating a agent
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    metadata: dict[str, Any] | None = None
    name: Annotated[
        str,
        Field(
            "",
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the agent
    """
    about: str = ""
    """
    About the agent
    """
    model: str = ""
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """
    instructions: str | list[str] = ""
    """
    Instructions for the agent
    """
    default_settings: DefaultChatSettings | None = None
    """
    Default settings for all sessions created by this agent
    """
