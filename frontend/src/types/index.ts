export interface Produtor {
  id: number;
  cpf_cnpj: string;
  nome: string;
  fazendas: Fazenda[];
  created_at: string;
  updated_at?: string;
}

export interface Fazenda {
  id: number;
  nome: string;
  cidade: string;
  estado: string;
  area_total: number;
  area_agricultavel: number;
  area_vegetacao: number;
  produtor_id: number;
  culturas: Cultura[];
  created_at: string;
  updated_at?: string;
}

export interface Cultura {
  id: number;
  nome: string;
  safra: string;
  fazenda_id: number;
  created_at: string;
  updated_at?: string;
}

export interface ProdutorCreate {
  cpf_cnpj: string;
  nome: string;
  fazendas?: FazendaCreate[];
}

export interface FazendaCreate {
  nome: string;
  cidade: string;
  estado: string;
  area_total: number;
  area_agricultavel: number;
  area_vegetacao: number;
  culturas?: CulturaCreate[];
}

export interface CulturaCreate {
  nome: string;
  safra: string;
}

export interface ProdutorUpdate {
  nome?: string;
}

export interface FazendaUpdate {
  nome?: string;
  cidade?: string;
  estado?: string;
  area_total?: number;
  area_agricultavel?: number;
  area_vegetacao?: number;
}

export interface DashboardStats {
  total_fazendas: number;
  total_hectares: number;
  por_estado: Record<string, number>;
  por_cultura: Record<string, number>;
  por_uso_solo: Record<string, number>;
}

export interface ApiResponse<T> {
  data: T;
  message?: string;
  error?: string;
} 