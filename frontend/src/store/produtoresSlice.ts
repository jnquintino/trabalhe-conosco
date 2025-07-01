import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { Produtor, ProdutorCreate, ProdutorUpdate, Fazenda, FazendaCreate, Cultura, CulturaCreate } from '@/types';
import { api } from '@/utils/api';

interface ProdutoresState {
  produtores: Produtor[];
  loading: boolean;
  error: string | null;
  selectedProdutor: Produtor | null;
}

const initialState: ProdutoresState = {
  produtores: [],
  loading: false,
  error: null,
  selectedProdutor: null,
};

// Async thunks
export const fetchProdutores = createAsyncThunk(
  'produtores/fetchProdutores',
  async () => {
    const response = await api.get<Produtor[]>('/produtores/');
    return response.data;
  }
);

export const createProdutor = createAsyncThunk(
  'produtores/createProdutor',
  async (produtor: ProdutorCreate) => {
    const response = await api.post<Produtor>('/produtores/', produtor);
    return response.data;
  }
);

export const updateProdutor = createAsyncThunk(
  'produtores/updateProdutor',
  async ({ id, data }: { id: number; data: ProdutorUpdate }) => {
    const response = await api.put<Produtor>(`/produtores/${id}`, data);
    return response.data;
  }
);

export const deleteProdutor = createAsyncThunk(
  'produtores/deleteProdutor',
  async (id: number) => {
    await api.delete(`/produtores/${id}`);
    return id;
  }
);

export const fetchProdutor = createAsyncThunk(
  'produtores/fetchProdutor',
  async (id: number) => {
    const response = await api.get<Produtor>(`/produtores/${id}`);
    return response.data;
  }
);

export const createFazenda = createAsyncThunk(
  'produtores/createFazenda',
  async ({ produtorId, fazenda }: { produtorId: number; fazenda: FazendaCreate }) => {
    const response = await api.post<Fazenda>(`/produtores/${produtorId}/fazendas/`, fazenda);
    return response.data;
  }
);

export const createCultura = createAsyncThunk(
  'produtores/createCultura',
  async ({ fazendaId, cultura }: { fazendaId: number; cultura: CulturaCreate }) => {
    const response = await api.post<Cultura>(`/fazendas/${fazendaId}/culturas/`, cultura);
    return response.data;
  }
);

const produtoresSlice = createSlice({
  name: 'produtores',
  initialState,
  reducers: {
    setSelectedProdutor: (state, action: PayloadAction<Produtor | null>) => {
      state.selectedProdutor = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch produtores
      .addCase(fetchProdutores.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProdutores.fulfilled, (state, action) => {
        state.loading = false;
        state.produtores = action.payload;
      })
      .addCase(fetchProdutores.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Erro ao carregar produtores';
      })
      // Create produtor
      .addCase(createProdutor.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(createProdutor.fulfilled, (state, action) => {
        state.loading = false;
        state.produtores.push(action.payload);
      })
      .addCase(createProdutor.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Erro ao criar produtor';
      })
      // Update produtor
      .addCase(updateProdutor.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(updateProdutor.fulfilled, (state, action) => {
        state.loading = false;
        const index = state.produtores.findIndex(p => p.id === action.payload.id);
        if (index !== -1) {
          state.produtores[index] = action.payload;
        }
        if (state.selectedProdutor?.id === action.payload.id) {
          state.selectedProdutor = action.payload;
        }
      })
      .addCase(updateProdutor.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Erro ao atualizar produtor';
      })
      // Delete produtor
      .addCase(deleteProdutor.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(deleteProdutor.fulfilled, (state, action) => {
        state.loading = false;
        state.produtores = state.produtores.filter(p => p.id !== action.payload);
        if (state.selectedProdutor?.id === action.payload) {
          state.selectedProdutor = null;
        }
      })
      .addCase(deleteProdutor.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Erro ao deletar produtor';
      })
      // Fetch produtor
      .addCase(fetchProdutor.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProdutor.fulfilled, (state, action) => {
        state.loading = false;
        state.selectedProdutor = action.payload;
      })
      .addCase(fetchProdutor.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Erro ao carregar produtor';
      });
  },
});

export const { setSelectedProdutor, clearError } = produtoresSlice.actions;
export default produtoresSlice.reducer; 