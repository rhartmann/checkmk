<!--
Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
conditions defined in the file COPYING, which is part of this source code package.
-->
<script setup lang="ts">
// TODO: move this file CMK-19774
import { ref } from 'vue'
import type { List } from '@/form/components/vue_formspec_components'
import FormList from '@/form/components/forms/FormList.vue'
const spec = ref<List>({
  type: 'list',
  title: 'some title',
  help: 'some help',
  validators: [],
  element_default_value: '',
  editable_order: true,
  add_element_label: 'some add element label',
  remove_element_label: 'some remove label',
  no_element_label: 'some no element label',
  element_template: {
    type: 'string',
    title: 'some title',
    help: 'some help',
    validators: []
  }
})
const data = ref<Array<string>>([])
</script>

<template>
  <FormList v-model:data="data" :spec="spec" :backend-validation="[]" />
</template>
