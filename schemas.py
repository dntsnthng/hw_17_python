get_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "page": {
      "type": "integer"
    },
    "per_page": {
      "type": "integer"
    },
    "total": {
      "type": "integer"
    },
    "total_pages": {
      "type": "integer"
    },
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "email": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "avatar": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "email": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "avatar": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "email": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "avatar": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "email": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "avatar": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar"
          ]
        }
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "page",
    "per_page",
    "total",
    "total_pages",
    "data",
    "support"
  ]
}

post_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "createdAt"
  ]
}

put_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "updatedAt"
  ]
}

post_login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}

list_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "page": {
      "type": "integer"
    },
    "per_page": {
      "type": "integer"
    },
    "total": {
      "type": "integer"
    },
    "total_pages": {
      "type": "integer"
    },
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        },
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            },
            "color": {
              "type": "string"
            },
            "pantone_value": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "year",
            "color",
            "pantone_value"
          ]
        }
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "page",
    "per_page",
    "total",
    "total_pages",
    "data",
    "support"
  ]
}

post_create = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "createdAt"
  ]
}

delayed_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "page": {
      "type": "integer"
    },
    "per_page": {
      "type": "integer"
    },
    "total": {
      "type": "integer"
    },
    "total_pages": {
      "type": "integer"
    },
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "email": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "avatar": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar"
          ]
        }
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "page",
    "per_page",
    "total",
    "total_pages",
    "data",
    "support"
  ]
}