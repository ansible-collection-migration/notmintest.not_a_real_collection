from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import MagicMock
from ansible.utils.path import unfrackpath


mock_unfrackpath_noop = MagicMock(spec_set=unfrackpath, side_effect=lambda x, *args, **kwargs: x)
