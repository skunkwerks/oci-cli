# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('ai.ai_root_group.command_name', 'ai'), cls=CommandGroupWithAlias, help=cli_util.override('ai.ai_root_group.help', """OCI Language Service solutions can help enterprise customers integrate AI into their products immediately using our proven,
pre-trained and custom models or containers, without a need to set up an house team of AI and ML experts.
This allows enterprises to focus on business drivers and development work rather than AI and ML operations, which shortens the time to market."""), short_help=cli_util.override('ai.ai_root_group.short_help', """Language API"""))
@cli_util.help_option_group
def ai_root_group():
    pass


@click.command(cli_util.override('ai.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('ai.endpoint_group.command_name', 'endpoint'), cls=CommandGroupWithAlias, help="""Description of the endpoint.""")
@cli_util.help_option_group
def endpoint_group():
    pass


@click.command(cli_util.override('ai.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('ai.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""Project enable users to organize their project resources.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('ai.model_group.command_name', 'model'), cls=CommandGroupWithAlias, help="""Description of the a Model.""")
@cli_util.help_option_group
def model_group():
    pass


@click.command(cli_util.override('ai.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('ai.evaluation_result_collection_group.command_name', 'evaluation-result-collection'), cls=CommandGroupWithAlias, help="""Results of a model evaluation analysis search. Contains EvaluationResultSummary items.""")
@cli_util.help_option_group
def evaluation_result_collection_group():
    pass


@click.command(cli_util.override('ai.detect_language_sentiments_group.command_name', 'detect-language-sentiments'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def detect_language_sentiments_group():
    pass


@click.command(cli_util.override('ai.batch_language_translation_group.command_name', 'batch-language-translation'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_language_translation_group():
    pass


@click.command(cli_util.override('ai.batch_detect_language_sentiments_group.command_name', 'batch-detect-language-sentiments'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_detect_language_sentiments_group():
    pass


@click.command(cli_util.override('ai.detect_language_entities_group.command_name', 'detect-language-entities'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def detect_language_entities_group():
    pass


@click.command(cli_util.override('ai.detect_language_text_classification_group.command_name', 'detect-language-text-classification'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def detect_language_text_classification_group():
    pass


@click.command(cli_util.override('ai.batch_detect_dominant_language_group.command_name', 'batch-detect-dominant-language'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_detect_dominant_language_group():
    pass


@click.command(cli_util.override('ai.batch_detect_language_key_phrases_group.command_name', 'batch-detect-language-key-phrases'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_detect_language_key_phrases_group():
    pass


@click.command(cli_util.override('ai.detect_dominant_language_group.command_name', 'detect-dominant-language'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def detect_dominant_language_group():
    pass


@click.command(cli_util.override('ai.detect_language_key_phrases_group.command_name', 'detect-language-key-phrases'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def detect_language_key_phrases_group():
    pass


@click.command(cli_util.override('ai.batch_detect_language_entities_group.command_name', 'batch-detect-language-entities'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_detect_language_entities_group():
    pass


@click.command(cli_util.override('ai.batch_detect_language_text_classification_group.command_name', 'batch-detect-language-text-classification'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def batch_detect_language_text_classification_group():
    pass


ai_root_group.add_command(work_request_log_group)
ai_root_group.add_command(endpoint_group)
ai_root_group.add_command(work_request_error_group)
ai_root_group.add_command(project_group)
ai_root_group.add_command(model_group)
ai_root_group.add_command(work_request_group)
ai_root_group.add_command(evaluation_result_collection_group)
ai_root_group.add_command(detect_language_sentiments_group)
ai_root_group.add_command(batch_language_translation_group)
ai_root_group.add_command(batch_detect_language_sentiments_group)
ai_root_group.add_command(detect_language_entities_group)
ai_root_group.add_command(detect_language_text_classification_group)
ai_root_group.add_command(batch_detect_dominant_language_group)
ai_root_group.add_command(batch_detect_language_key_phrases_group)
ai_root_group.add_command(detect_dominant_language_group)
ai_root_group.add_command(detect_language_key_phrases_group)
ai_root_group.add_command(batch_detect_language_entities_group)
ai_root_group.add_command(batch_detect_language_text_classification_group)


@batch_detect_dominant_language_group.command(name=cli_util.override('ai.batch_detect_dominant_language.command_name', 'batch-detect-dominant-language'), help=u"""The API returns the detected language and a related confidence score (between 0 and 1).  It supports passing a batch of records.

[List of supported languages.]

Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchDetectDominantLanguage)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Documents for detect language.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[DominantLanguageDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[DominantLanguageDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchDetectDominantLanguageResult'})
@cli_util.wrap_exceptions
def batch_detect_dominant_language(ctx, from_json, documents, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_detect_dominant_language(
        batch_detect_dominant_language_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@batch_detect_language_entities_group.command(name=cli_util.override('ai.batch_detect_language_entities.command_name', 'batch-detect-language-entities'), help=u"""The API extracts entities in text records. For each entity, its type/subtype and confidence score (between 0 and 1) is returned.  It supports passing a batch of records.

[List of supported entities.]

Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchDetectLanguageEntities)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Documents for detect entities.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@cli_util.option('--endpoint-id', help=u"""The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchDetectLanguageEntitiesResult'})
@cli_util.wrap_exceptions
def batch_detect_language_entities(ctx, from_json, documents, compartment_id, endpoint_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if endpoint_id is not None:
        _details['endpointId'] = endpoint_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_detect_language_entities(
        batch_detect_language_entities_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@batch_detect_language_key_phrases_group.command(name=cli_util.override('ai.batch_detect_language_key_phrases.command_name', 'batch-detect-language-key-phrases'), help=u"""The API extracts key-phrases in text records. For each key-phrase, a score (between 0 and 1) is returned that highlights the importance of the key-phrase in the context of the text.  It supports passing a batch of records.

Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchDetectLanguageKeyPhrases)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Documents for detect keyPhrases.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchDetectLanguageKeyPhrasesResult'})
@cli_util.wrap_exceptions
def batch_detect_language_key_phrases(ctx, from_json, documents, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_detect_language_key_phrases(
        batch_detect_language_key_phrases_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@batch_detect_language_sentiments_group.command(name=cli_util.override('ai.batch_detect_language_sentiments.command_name', 'batch-detect-language-sentiments'), help=u"""The API extracts aspect-based and sentence level sentiment in text records.

For aspect-based sentiment analysis, a set of aspects and their respective sentiment is returned for each record. Similarly, for sentence-level sentiment analysis, the sentiment is returned at the sentence level.

For sentiment analysis, confidence scores are provided for each of the classes (positive, negative, neutral and mixed).

Learn more about sentiment analysis [here].

Limitations:  - A batch may have up to 100 records.  - A record may be up to 5000 characters long.  - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchDetectLanguageSentiments)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Documents for detect sentiments.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@cli_util.option('--level', type=custom_types.CliCaseInsensitiveChoice(["ASPECT", "SENTENCE"]), multiple=True, help=u"""Set this parameter for sentence and aspect level sentiment analysis. Allowed values are:    - ASPECT    - SENTENCE""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchDetectLanguageSentimentsResult'})
@cli_util.wrap_exceptions
def batch_detect_language_sentiments(ctx, from_json, documents, compartment_id, level):

    kwargs = {}
    if level is not None and len(level) > 0:
        kwargs['level'] = level
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_detect_language_sentiments(
        batch_detect_language_sentiments_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@batch_detect_language_text_classification_group.command(name=cli_util.override('ai.batch_detect_language_text_classification.command_name', 'batch-detect-language-text-classification'), help=u"""The API automatically classifies text into a set of pre-determined classes and sub-classes. A single class/subclass is returned for each record classified.

It supports passing a batch of records.

Learn more about text classification [here].

Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchDetectLanguageTextClassification)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Documents for detect text classification.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@cli_util.option('--endpoint-id', help=u"""The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchDetectLanguageTextClassificationResult'})
@cli_util.wrap_exceptions
def batch_detect_language_text_classification(ctx, from_json, documents, compartment_id, endpoint_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if endpoint_id is not None:
        _details['endpointId'] = endpoint_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_detect_language_text_classification(
        batch_detect_language_text_classification_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@batch_language_translation_group.command(name=cli_util.override('ai.batch_language_translation.command_name', 'batch-language-translation'), help=u"""Translate text to other language over pre-deployed model. Use state of the art neural machine translation to translate text between more than 15 languages. Limitations:   - A batch may have up to 100 records.   - A record may be up to 5000 characters long.   - The total of characters to process in a request can be up to 20,000 characters. \n[Command Reference](batchLanguageTranslation)""")
@cli_util.option('--documents', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of documents for translation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment that calls the API, inference will be served from pre trained model""")
@cli_util.option('--target-language-code', help=u"""Language code per the [ISO 639-1] standard.""")
@json_skeleton_utils.get_cli_json_input_option({'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'documents': {'module': 'ai_language', 'class': 'list[TextDocument]'}}, output_type={'module': 'ai_language', 'class': 'BatchLanguageTranslationResult'})
@cli_util.wrap_exceptions
def batch_language_translation(ctx, from_json, documents, compartment_id, target_language_code):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['documents'] = cli_util.parse_json_parameter("documents", documents)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if target_language_code is not None:
        _details['targetLanguageCode'] = target_language_code

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.batch_language_translation(
        batch_language_translation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.change_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a Endpoint into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeEndpointCompartment)""")
@cli_util.option('--endpoint-id', required=True, help=u"""The OCID of the endpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_endpoint_compartment(ctx, from_json, endpoint_id, compartment_id, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.change_endpoint_compartment(
        endpoint_id=endpoint_id,
        change_endpoint_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.change_model_compartment.command_name', 'change-compartment'), help=u"""Moves a Model into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeModelCompartment)""")
@cli_util.option('--model-id', required=True, help=u"""unique model OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_model_compartment(ctx, from_json, model_id, compartment_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.change_model_compartment(
        model_id=model_id,
        change_model_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.change_project_compartment.command_name', 'change-compartment'), help=u"""Moves a Project into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeProjectCompartment)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the project.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_project_compartment(ctx, from_json, project_id, compartment_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.change_project_compartment(
        project_id=project_id,
        change_project_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.create_endpoint.command_name', 'create'), help=u"""Creates a new endpoint and deploy the trained model \n[Command Reference](createEndpoint)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] compartment identifier for the endpoint""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model to associate with the endpoint.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the an endpoint.""")
@cli_util.option('--inference-units', type=click.INT, help=u"""Number of replicas required for this endpoint. This will be optional parameter. Default will be 1.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_language', 'class': 'Endpoint'})
@cli_util.wrap_exceptions
def create_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, model_id, display_name, description, inference_units, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['modelId'] = model_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if inference_units is not None:
        _details['inferenceUnits'] = inference_units

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_endpoint(
        create_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model.command_name', 'create'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--model-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--training-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--test-strategy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, model_details, training_dataset, display_name, description, test_strategy, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)
    _details['trainingDataset'] = cli_util.parse_json_parameter("training_dataset", training_dataset)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if test_strategy is not None:
        _details['testStrategy'] = cli_util.parse_json_parameter("test_strategy", test_strategy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model_named_entity_recognition_model_details.command_name', 'create-model-named-entity-recognition-model-details'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--training-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--test-strategy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--model-details-language-code', help=u"""supported language default value is en""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model_named_entity_recognition_model_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, training_dataset, display_name, description, test_strategy, freeform_tags, defined_tags, model_details_language_code):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['trainingDataset'] = cli_util.parse_json_parameter("training_dataset", training_dataset)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if test_strategy is not None:
        _details['testStrategy'] = cli_util.parse_json_parameter("test_strategy", test_strategy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if model_details_language_code is not None:
        _details['modelDetails']['languageCode'] = model_details_language_code

    _details['modelDetails']['modelType'] = 'NAMED_ENTITY_RECOGNITION'

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model_text_classification_model_details.command_name', 'create-model-text-classification-model-details'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--training-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--test-strategy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--model-details-language-code', help=u"""supported language default value is en""")
@cli_util.option('--model-details-classification-mode', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'model-details-classification-mode': {'module': 'ai_language', 'class': 'ClassificationType'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'model-details-classification-mode': {'module': 'ai_language', 'class': 'ClassificationType'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model_text_classification_model_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, training_dataset, display_name, description, test_strategy, freeform_tags, defined_tags, model_details_language_code, model_details_classification_mode):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['trainingDataset'] = cli_util.parse_json_parameter("training_dataset", training_dataset)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if test_strategy is not None:
        _details['testStrategy'] = cli_util.parse_json_parameter("test_strategy", test_strategy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if model_details_language_code is not None:
        _details['modelDetails']['languageCode'] = model_details_language_code

    if model_details_classification_mode is not None:
        _details['modelDetails']['classificationMode'] = cli_util.parse_json_parameter("model_details_classification_mode", model_details_classification_mode)

    _details['modelDetails']['modelType'] = 'TEXT_CLASSIFICATION'

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model_data_science_labeling_dataset.command_name', 'create-model-data-science-labeling-dataset'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--model-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--training-dataset-dataset-id', required=True, help=u"""Data Science Labelling Service OCID""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--test-strategy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model_data_science_labeling_dataset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, model_details, training_dataset_dataset_id, display_name, description, test_strategy, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['trainingDataset'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)
    _details['trainingDataset']['datasetId'] = training_dataset_dataset_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if test_strategy is not None:
        _details['testStrategy'] = cli_util.parse_json_parameter("test_strategy", test_strategy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['trainingDataset']['datasetType'] = 'DATA_SCIENCE_LABELING'

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model_object_storage_dataset.command_name', 'create-model-object-storage-dataset'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--model-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--training-dataset-location-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--test-strategy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'training-dataset-location-details': {'module': 'ai_language', 'class': 'LocationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'test-strategy': {'module': 'ai_language', 'class': 'TestStrategy'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'training-dataset-location-details': {'module': 'ai_language', 'class': 'LocationDetails'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model_object_storage_dataset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, model_details, training_dataset_location_details, display_name, description, test_strategy, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['trainingDataset'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)
    _details['trainingDataset']['locationDetails'] = cli_util.parse_json_parameter("training_dataset_location_details", training_dataset_location_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if test_strategy is not None:
        _details['testStrategy'] = cli_util.parse_json_parameter("test_strategy", test_strategy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['trainingDataset']['datasetType'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.create_model_test_and_validation_dataset_strategy.command_name', 'create-model-test-and-validation-dataset-strategy'), help=u"""Creates a new model for training and train the model with date provided. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  for the models compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--model-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--training-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-strategy-testing-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-strategy-validation-dataset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'test-strategy-testing-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy-validation-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_language', 'class': 'ModelDetails'}, 'training-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}, 'test-strategy-testing-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}, 'test-strategy-validation-dataset': {'module': 'ai_language', 'class': 'DatasetDetails'}}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model_test_and_validation_dataset_strategy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, model_details, training_dataset, test_strategy_testing_dataset, display_name, description, freeform_tags, defined_tags, test_strategy_validation_dataset):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['testStrategy'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)
    _details['trainingDataset'] = cli_util.parse_json_parameter("training_dataset", training_dataset)
    _details['testStrategy']['testingDataset'] = cli_util.parse_json_parameter("test_strategy_testing_dataset", test_strategy_testing_dataset)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if test_strategy_validation_dataset is not None:
        _details['testStrategy']['validationDataset'] = cli_util.parse_json_parameter("test_strategy_validation_dataset", test_strategy_validation_dataset)

    _details['testStrategy']['strategyType'] = 'TEST_AND_VALIDATION_DATASET'

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.create_project.command_name', 'create'), help=u"""Creates a new Project. \n[Command Reference](createProject)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] for the project's compartment.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_language', 'class': 'Project'})
@cli_util.wrap_exceptions
def create_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.create_project(
        create_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.delete_endpoint.command_name', 'delete'), help=u"""Deletes a provisioned endpoint resource by identifier. This operation fails with a 409 error unless all associated resources are in a DELETED state. You must delete all associated resources before deleting a model. \n[Command Reference](deleteEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""The OCID of the endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.delete_endpoint(
        endpoint_id=endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.delete_model.command_name', 'delete'), help=u"""Deletes a provisioned model resource by identifier. This operation fails with a 409 error unless all associated resources are in a DELETED state. You must delete all associated resources before deleting a model. \n[Command Reference](deleteModel)""")
@cli_util.option('--model-id', required=True, help=u"""unique model OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.delete_model(
        model_id=model_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.delete_project.command_name', 'delete'), help=u"""Deletes a Project resource by identifier. This operation fails with a 409 error unless all associated resources (models deployments or data assets) are in a DELETED state. You must delete all associated resources before deleting a project. \n[Command Reference](deleteProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the project.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.delete_project(
        project_id=project_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@detect_dominant_language_group.command(name=cli_util.override('ai.detect_dominant_language.command_name', 'detect-dominant-language'), help=u"""The API returns the detected language and a related confidence score (between 0 and 1).

[List of supported languages.]

Limitations: - A record may be up to 1000 characters long. \n[Command Reference](detectDominantLanguage)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect language.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectDominantLanguageResult'})
@cli_util.wrap_exceptions
def detect_dominant_language(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_dominant_language(
        detect_dominant_language_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_entities_group.command(name=cli_util.override('ai.detect_language_entities.command_name', 'detect-language-entities'), help=u"""The API extracts entities in text records. For each entity, its type and confidence score (between 0 and 1) is returned.

Limitations: - A text may be up to 1000 characters long. \n[Command Reference](detectLanguageEntities)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect entities.""")
@cli_util.option('--model-version', type=custom_types.CliCaseInsensitiveChoice(["V2_1", "V1_1"]), help=u"""Named Entity Recognition model versions. By default user will get output from V2.1 implementation.""")
@cli_util.option('--is-pii', type=click.BOOL, help=u"""If this parameter is set to true, you only get PII (Personally identifiable information) entities like PhoneNumber, Email, Person, and so on. Default value is false.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageEntitiesResult'})
@cli_util.wrap_exceptions
def detect_language_entities(ctx, from_json, text, model_version, is_pii):

    kwargs = {}
    if model_version is not None:
        kwargs['model_version'] = model_version
    if is_pii is not None:
        kwargs['is_pii'] = is_pii
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_entities(
        detect_language_entities_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_key_phrases_group.command(name=cli_util.override('ai.detect_language_key_phrases.command_name', 'detect-language-key-phrases'), help=u"""The API extracts key-phrases in text records. For each key-phrase, a score (between 0 and 1) is returned that highlights the importance of the key-phrase in the context of the text.

Limitations: - A record may be up to 1000 characters long. \n[Command Reference](detectLanguageKeyPhrases)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect keyPhrases.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageKeyPhrasesResult'})
@cli_util.wrap_exceptions
def detect_language_key_phrases(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_key_phrases(
        detect_language_key_phrases_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_sentiments_group.command(name=cli_util.override('ai.detect_language_sentiments.command_name', 'detect-language-sentiments'), help=u"""The API extracts aspect-based in text records.

For aspect-based sentiment analysis, a set of aspects and their respective sentiment is returned.

For sentiment analysis, confidence scores are provided for each of the classes (positive, negative, neutral).

Learn more about sentiment analysis [here].

Limitations:  - A record may be up to 1000 characters long. \n[Command Reference](detectLanguageSentiments)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect sentiments.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageSentimentsResult'})
@cli_util.wrap_exceptions
def detect_language_sentiments(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_sentiments(
        detect_language_sentiments_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_text_classification_group.command(name=cli_util.override('ai.detect_language_text_classification.command_name', 'detect-language-text-classification'), help=u"""The API automatically classifies text into a set of pre-determined classes and sub-classes. A single class/subclass is returned for each record classified.

Learn more about text classification [here].

Limitations: - A record may be up to 1000 characters long. \n[Command Reference](detectLanguageTextClassification)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect text classes.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageTextClassificationResult'})
@cli_util.wrap_exceptions
def detect_language_text_classification(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_text_classification(
        detect_language_text_classification_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.get_endpoint.command_name', 'get'), help=u"""Gets an endpoint by identifier \n[Command Reference](getEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""The OCID of the endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'Endpoint'})
@cli_util.wrap_exceptions
def get_endpoint(ctx, from_json, endpoint_id):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.get_endpoint(
        endpoint_id=endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.get_model.command_name', 'get'), help=u"""Gets a model by identifier \n[Command Reference](getModel)""")
@cli_util.option('--model-id', required=True, help=u"""unique model OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'Model'})
@cli_util.wrap_exceptions
def get_model(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.get_model(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.get_project.command_name', 'get'), help=u"""Gets a Project by identifier \n[Command Reference](getProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the project.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, project_id):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.get_project(
        project_id=project_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('ai.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.list_endpoints.command_name', 'list'), help=u"""Returns a list of Endpoints. \n[Command Reference](listEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--endpoint-id', help=u"""The OCID of the endpoint.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--model-id', help=u"""The ID of the trained model for which to list the endpoints.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'EndpointCollection'})
@cli_util.wrap_exceptions
def list_endpoints(ctx, from_json, all_pages, page_size, compartment_id, endpoint_id, project_id, display_name, model_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if model_id is not None:
        kwargs['model_id'] = model_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@evaluation_result_collection_group.command(name=cli_util.override('ai.list_evaluation_results.command_name', 'list-evaluation-results'), help=u"""Get a (paginated) list of evaluation results for a given model. \n[Command Reference](listEvaluationResults)""")
@cli_util.option('--model-id', required=True, help=u"""unique model OCID.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'EvaluationResultCollection'})
@cli_util.wrap_exceptions
def list_evaluation_results(ctx, from_json, all_pages, page_size, model_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_evaluation_results,
            model_id=model_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_evaluation_results,
            limit,
            page_size,
            model_id=model_id,
            **kwargs
        )
    else:
        result = client.list_evaluation_results(
            model_id=model_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.list_models.command_name', 'list'), help=u"""Returns a list of models. \n[Command Reference](listModels)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--model-id', help=u"""unique model OCID.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'ModelCollection'})
@cli_util.wrap_exceptions
def list_models(ctx, from_json, all_pages, page_size, compartment_id, model_id, project_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if model_id is not None:
        kwargs['model_id'] = model_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_models,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_models,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_models(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.list_projects.command_name', 'list'), help=u"""Returns a list of  Projects. \n[Command Reference](listProjects)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'ProjectCollection'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, project_id, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if project_id is not None:
        kwargs['project_id'] = project_id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_projects,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_projects,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_projects(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('ai.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_group.command(name=cli_util.override('ai.list_work_request_logs.command_name', 'list'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'WorkRequestLogCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('ai.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource for which list workrequests.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, page, limit, resource_id, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('ai.update_endpoint.command_name', 'update'), help=u"""Update the Endpoint identified by the id \n[Command Reference](updateEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""The OCID of the endpoint.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the endpoint.""")
@cli_util.option('--model-id', help=u"""The [OCID] of the model to associate with the endpoint.""")
@cli_util.option('--inference-units', type=click.INT, help=u"""Number of replicas required for this endpoint. This will be optional parameter.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, display_name, description, model_id, inference_units, freeform_tags, defined_tags, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if model_id is not None:
        _details['modelId'] = model_id

    if inference_units is not None:
        _details['inferenceUnits'] = inference_units

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.update_endpoint(
        endpoint_id=endpoint_id,
        update_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai.update_model.command_name', 'update'), help=u"""Updates the model \n[Command Reference](updateModel)""")
@cli_util.option('--model-id', required=True, help=u"""unique model OCID.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the a model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_model(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.update_model(
        model_id=model_id,
        update_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai.update_project.command_name', 'update'), help=u"""Updates the Project \n[Command Reference](updateProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the project.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_language', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_language', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_project(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.update_project(
        project_id=project_id,
        update_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
